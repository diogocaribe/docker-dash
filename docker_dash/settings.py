from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )

    pg_dsn: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'

    DEBUG_MODE: bool
