from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from db.connection import create_pool, close_pool, get_connection
import aioodbc

# 애플리케이션 시작/종료 시점에 커넥션 풀을 관리합니다.
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 애플리케이션 시작 시 커넥션 풀 생성
    await create_pool()
    yield
    # 애플리케이션 종료 시 커넥션 풀 해제
    await close_pool()

app = FastAPI(lifespan=lifespan, title="FastAPI ODBC API")

from api.airport.routes import router as airport_router
from api.flight.routes import router as flight_router
from api.noise.routes import router as noise_router
from api.parking.routes import router as parking_router

app.include_router(airport_router, prefix="/api")
app.include_router(flight_router, prefix="/api")
app.include_router(noise_router, prefix="/api")
app.include_router(parking_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Service is running"}

@app.get("/data")
async def get_data(conn: aioodbc.Connection = Depends(get_connection)):
    """
    커넥션 풀을 통해 주입받은 비동기 ODBC 커넥션으로 데이터를 조회하는 예제입니다.
    """
    async with conn.cursor() as cur:
        # 쿼리 예시 (실제 스키마에 맞게 변경 필요)
        # await cur.execute("SELECT TOP 10 id, name FROM some_table")
        # rows = await cur.fetchall()
        # return [{"id": row[0], "name": row[1]} for row in rows]
        
        return {"status": "Database connection successful, ready to fetch data"}
