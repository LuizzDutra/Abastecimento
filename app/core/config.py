from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DB_URL: str = ""
    VERSION: str = "V1.0.0"

    model_config = SettingsConfigDict(env_file="./.env")


@lru_cache
def config() -> Config:
    return Config()
