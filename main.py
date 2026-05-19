import time
import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from core.utils import json_to_xml, transform_for_json

from core.logging_config import setup_logging
from db.connection import create_pool, close_pool, get_connection, db_pool
import aioodbc

# ── 로깅 초기화 (가장 먼저) ───────────────────────────────────────────
setup_logging()

logger = logging.getLogger(__name__)
access_logger = logging.getLogger("api.access")


# ── Lifespan ──────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_pool()
    try:
        async with db_pool.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 1 FROM DUAL")
                await cur.fetchone()
                logger.info("Database connection test successful.")
    except Exception as e:
        logger.error(f"Database connection test failed: {e}")
        # [의도적 설계] DB 연결 실패 시 앱 기동 자체를 중단.
        # 불완전한 상태로 요청을 받는 것보다 명시적 실패가 안전하다고 판단.
        # DB 재시작 시 앱도 함께 재시작되어야 하는 운영 정책을 전제로 함.
        raise
    yield
    await close_pool()


# ── FastAPI 앱 ────────────────────────────────────────────────────────
app = FastAPI(
    lifespan=lifespan,
    title="FastAPI Public API",
    # 프로덕션에서는 docs 비활성화 고려
    # docs_url=None, redoc_url=None,
)


# ── CORS ──────────────────────────────────────────────────────────────
# 불특정 다수 대상 공공 데이터 API:
#   allow_origins=["*"]  → 모든 도메인 허용 (공공 개방 필수)
#   allow_credentials=False → 쿠키/인증헤더 불필요, wildcard와 조합 가능
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],       # 조회 전용 API이므로 GET만 허용
    allow_headers=["*"],
)


# ── Access Log 미들웨어 ───────────────────────────────────────────────
# [주의] FastAPI의 exception_handler는 미들웨어 안쪽에서 예외를 response로 변환한다.
# 따라서 call_next()는 거의 예외를 던지지 않고 이미 처리된 response를 반환한다.
# 500 에러 로깅은 try/except 대신 response.status_code로 판단한다.
@app.middleware("http")
async def access_log_middleware(request: Request, call_next):
    start = time.perf_counter()
    client_ip = request.headers.get("X-Forwarded-For", request.client.host if request.client else "-")
    response = await call_next(request)
    elapsed_ms = (time.perf_counter() - start) * 1000
    log_fn = access_logger.error if response.status_code >= 500 else access_logger.info
    log_fn(
        f'{client_ip} "{request.method} {request.url.path}" '
        f'{response.status_code} {elapsed_ms:.1f}ms'
    )
    return response


# ── XML/JSON 변환 미들웨어 ────────────────────────────────────────────
@app.middleware("http")
async def response_format_middleware(request: Request, call_next):
    response = await call_next(request)
    if "application/json" not in response.headers.get("content-type", ""):
        return response

    body = b""
    async for chunk in response.body_iterator:
        body += chunk
    import json as _json
    data = _json.loads(body)

    cors_origin = response.headers.get("Access-Control-Allow-Origin", "*")
    request_type = request.query_params.get("type", "json")

    if request_type in ("xml", "XML"):
        return Response(
            content=json_to_xml(data),
            media_type="application/xml",
            status_code=response.status_code,
            headers={"Access-Control-Allow-Origin": cors_origin},
        )
    else:
        return Response(
            content=_json.dumps({"response": transform_for_json(data)}, ensure_ascii=False),
            media_type="application/json",
            status_code=response.status_code,
            headers={"Access-Control-Allow-Origin": cors_origin},
        )


# ── 전역 예외 핸들러 ─────────────────────────────────────────────────
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if isinstance(exc.detail, dict):
        content = {"header": exc.detail}
    else:
        content = {"header": {"resultCode": str(exc.status_code), "resultMessage": str(exc.detail)}}
    return JSONResponse(
        status_code=exc.status_code,
        content=content,
        headers={"Access-Control-Allow-Origin": "*"},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """파라미터 유효성 검사 실패 (422) → 클라이언트 친화적 메시지 반환"""
    errors = [{"field": ".".join(str(l) for l in e["loc"]), "message": e["msg"]} for e in exc.errors()]
    return JSONResponse(
        status_code=422,
        content={"header": {"resultCode": "01", "resultMessage": "요청 파라미터가 올바르지 않습니다.", "errors": errors}},
    )


@app.exception_handler(asyncio.TimeoutError)
async def timeout_exception_handler(request: Request, exc: asyncio.TimeoutError):
    """DB 쿼리 타임아웃 → 504 반환"""
    logger.error(f"Query timeout [{request.method} {request.url.path}]", exc_info=True)
    return JSONResponse(
        status_code=504,
        content={"header": {"resultCode": "98", "resultMessage": "처리 시간이 초과되었습니다. 잠시 후 다시 시도해 주세요."}},
        # CORSMiddleware가 일반 응답에는 헤더를 붙이지만,
        # 예외 핸들러 응답에는 FastAPI 버전에 따라 누락될 수 있어 명시적으로 추가.
        headers={"Access-Control-Allow-Origin": "*"},
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """그 외 모든 예외 → 500 반환, 상세 오류는 서버 로그에만 기록"""
    logger.error(f"Unhandled exception [{request.method} {request.url.path}]: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"header": {"resultCode": "99", "resultMessage": "서비스 오류가 발생했습니다. 잠시 후 다시 시도해 주세요."}},
        # CORSMiddleware가 일반 응답에는 헤더를 붙이지만,
        # 예외 핸들러 응답에는 FastAPI 버전에 따라 누락될 수 있어 명시적으로 추가.
        headers={"Access-Control-Allow-Origin": "*"},
    )


# ── 라우터 등록 ───────────────────────────────────────────────────────
from api.public.routes.airport import router as airport_router
from api.public.routes.flight import router as flight_router
from api.public.routes.noise import router as noise_router
from api.public.routes.parking import router as parking_router

app.include_router(airport_router, prefix="/public")
app.include_router(flight_router, prefix="/public")
app.include_router(noise_router, prefix="/public")
app.include_router(parking_router, prefix="/public")


@app.get("/")
async def root():
    return {"message": "Service is running"}