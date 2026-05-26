from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_server: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    odbc_driver: str
    env: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
