from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Config(BaseSettings):
    #Ao usar docker compose o host será "db"
    DB_URL: str = "dialect+driver://username:password@host:port/database"

    #Usado para migrações no alembic criadas a partir da máquina local
    #É necessário trocar a porta para 5433 
    #ou outra que esteja configurada no docker-compose.yml
    LOCAL_DB_URL: str = "dialect+driver://username:password@host:port/database"

    VERSION: str = "V1.0.0"

    model_config = SettingsConfigDict(env_file="./.env")


@lru_cache
def config() -> Config:
    return Config()
