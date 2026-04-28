import asyncio
from db.connection import db_pool
from core.config import settings

async def main():
    print("====================================")
    print(f"Testing connection to Oracle DB:")
    print(f"Server: {settings.db_server}:{settings.db_port}")
    print(f"Service/DB Name: {settings.db_name}")
    print(f"User: {settings.db_user}")
    print("====================================")
    
    try:
        await db_pool.connect()
        async with db_pool.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT * FROM v$version")
                rows = await cursor.fetchall()
                print("\n✅ Connection Successful!")
                print("\n[Oracle Database Version]")
                for row in rows:
                    print(row[0])
    except Exception as e:
        print(f"\n❌ Connection failed: {e}")
    finally:
        await db_pool.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
