from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, Extra


class Settings(BaseSettings):
    PG_URI: PostgresDsn
    APP_TITLE: str
    APP_VERSION: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = Extra.allow
        env_prefix = "PIT_"


settings = Settings()
