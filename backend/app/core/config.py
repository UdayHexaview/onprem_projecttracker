from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    database_url: str = Field(default="sqlite:///./test.db", env="DATABASE_URL")

    class Config:
        env_file = ".env"

settings = Settings()