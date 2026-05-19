from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    API_URL: str = "http://localhost/api/v1/abastecimentos"
    REQUEST_QTT: int = 50
    PRINT: bool = True

    model_config = SettingsConfigDict(env_file="./.env")
