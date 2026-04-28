import aioodbc
import logging
from typing import AsyncGenerator
from core.config import settings

logger = logging.getLogger(__name__)

class DatabasePool:
    def __init__(self):
        self.pool = None

    async def connect(self):
        # DSN(Data Source Name) 문자열 구성
        # 데이터베이스 종류나 드라이버에 따라 형태가 다를 수 있습니다.
        dsn = (
            f"DRIVER={{{settings.odbc_driver}}};"
            f"DBQ={settings.db_server}:{settings.db_port}/{settings.db_name};"
            f"UID={settings.db_user};"
            f"PWD={settings.db_password};"
        )
        try:
            # aioodbc를 사용해 비동기 커넥션 풀을 생성합니다.
            # 다수의 호출이 발생하므로 적절한 minsize와 maxsize를 지정합니다.
            self.pool = await aioodbc.create_pool(
                dsn=dsn, 
                minsize=1, 
                maxsize=20, 
                pool_recycle=3600 # 1시간마다 커넥션 갱신 (유휴 커넥션 끊김 방지)
            )
            logger.info("ODBC connection pool created successfully.")
        except Exception as e:
            logger.error(f"Error creating ODBC connection pool: {e}")
            raise

    async def disconnect(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()
            logger.info("ODBC connection pool closed.")

db_pool = DatabasePool()

# Lifespan 이벤트를 위한 초기화 함수
async def create_pool():
    await db_pool.connect()

async def close_pool():
    await db_pool.disconnect()

# FastAPI 의존성(Dependency) 주입을 위한 제너레이터
async def get_connection() -> AsyncGenerator[aioodbc.Connection, None]:
    if not db_pool.pool:
        raise RuntimeError("Database pool is not initialized")
    
    # 커넥션 풀에서 비동기로 커넥션을 획득하고 사용이 끝나면 반환합니다.
    async with db_pool.pool.acquire() as conn:
        yield conn
