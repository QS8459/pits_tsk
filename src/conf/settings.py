from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, Extra


class Settings(BaseSettings):
    PG_URI: PostgresDsn

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = Extra.allow
        env_prefix = "PIT_"


settings = Settings()