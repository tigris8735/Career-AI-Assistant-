from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    # База данных
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/career_scout"
    
    # JWT
    JWT_SECRET: str = "your-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # DeepSeek API
    DEEPSEEK_API_KEY: Optional[str] = None
    DEEPSEEK_API_URL: str = "https://api.deepseek.com"
    DEEPSEEK_MODEL: str = "deepseek-chat"
    
    # HH.ru
    HH_RU_CLIENT_ID: Optional[str] = None
    HH_RU_CLIENT_SECRET: Optional[str] = None
    HH_RU_API_URL: str = "https://api.hh.ru"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Файлы
    UPLOAD_DIR: str = "./uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    
    # Приложение
    APP_NAME: str = "AI Career Scout"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()