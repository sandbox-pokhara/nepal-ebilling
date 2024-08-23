from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    DEBUG: bool = True
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_DB: str = "bs"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_PORT: int = 5432
    TIME_ZONE: str = "UTC"


ENV = Environment()
