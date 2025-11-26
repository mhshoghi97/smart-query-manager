from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql+asyncpg://admin:password@postgres:5432/query_manager";


    # Redis
    redis_url: str = "redis://redis:6379/0"

    # OpenAI
    openai_api_key: Optional[str] = None

    # Gemini API Key
    gemini_api_key: Optional[str] = None


    # App
    app_name: str = "Smart Query Manager"
    debug: bool = False
    log_level :str = "INFO"


    class Config:
        env_file = ".env"

settings = Settings()