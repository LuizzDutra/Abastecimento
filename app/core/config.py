from decimal import getcontext
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

#Configura precisão do Decimal
#Precisão suficiente para os precos(2) e volume(3)
getcontext().prec = 3


class Config(BaseSettings):
    #Ao usar docker compose o host será "db"
    DB_URL: str = "dialect+driver://username:password@host:port/database"
    VERSION: str = "V1.0.0"

    model_config = SettingsConfigDict(env_file="./.env")


@lru_cache
def config() -> Config:
    return Config()
