import asyncio
import aioodbc
import logging
from collections.abc import AsyncGenerator
from core.config import settings

logger = logging.getLogger(__name__)

# DB_ACQUIRE_TIMEOUT: create_pool(timeout=)과 일치시켜 사용
# DB_QUERY_TIMEOUT: 서비스/라우터 레이어의 cursor.execute() 시점에 asyncio.timeout()으로 적용
DB_ACQUIRE_TIMEOUT = 30
DB_QUERY_TIMEOUT = 30


class DatabasePool:
    def __init__(self):
        self.pool = None

    async def connect(self):
        dsn = (
            f"DRIVER={{{settings.odbc_driver}}};"
            f"DBQ={settings.db_server}:{settings.db_port}/{settings.db_name};"
            f"UID={settings.db_user};"
            f"PWD={settings.db_password};"
        )
        safe_dsn = dsn.replace(settings.db_password, "***")
        try:
            self.pool = await aioodbc.create_pool(
                dsn=dsn,
                minsize=1,
                maxsize=20,
                timeout=DB_ACQUIRE_TIMEOUT,  # 풀 내부 커넥션 획득 타임아웃
            )
            logger.info("ODBC connection pool created successfully.")
        except Exception as e:
            logger.error(f"Error creating ODBC connection pool: {e} | DSN: {safe_dsn}")
            raise

    async def disconnect(self):
        if not self.pool:
            logger.warning("disconnect() called but pool was never initialized.")
            return
        self.pool.close()
        await self.pool.wait_closed()
        self.pool = None
        logger.info("ODBC connection pool closed.")


db_pool = DatabasePool()


async def create_pool():
    await db_pool.connect()


async def close_pool():
    await db_pool.disconnect()


async def get_connection() -> AsyncGenerator[aioodbc.Connection, None]:
    """
    FastAPI Depends용 커넥션 제공 제너레이터.

    [설계 원칙]
    - 커넥션 획득 타임아웃은 create_pool(timeout=DB_ACQUIRE_TIMEOUT)에서 처리.
      이중으로 asyncio.timeout()을 감싸면 예외 처리가 복잡해지므로 제외.
    - 단일 쿼리 타임아웃(DB_QUERY_TIMEOUT)은 이 레이어에서 적용하지 않음.
      yield conn 전체를 감싸면 '단일 쿼리' 타임아웃이 아니라
      '전체 API 요청 처리 시간' 타임아웃으로 동작하기 때문.
      → 서비스/라우터 레이어에서 cursor.execute() 호출부에 직접 적용할 것:
        async with asyncio.timeout(DB_QUERY_TIMEOUT):
            await cursor.execute(...)
    - finally 블록으로 비즈니스 로직 완료 또는 예외 발생 시에도
      커넥션이 반드시 풀로 반환되도록 보장 (커넥션 누수 방지).
    """
    if not db_pool.pool:
        raise RuntimeError("Database pool is not initialized")

    conn = None
    try:
        conn = await db_pool.pool.acquire()
        yield conn
    except Exception as e:
        logger.error(f"Unexpected database connection error: {e}")
        raise
    finally:
        if conn is not None:
            await db_pool.pool.release(conn)
