from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    # Настройки приложения
    APP_NAME: str = "AI Career Scout"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Настройки базы данных
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/career_scout"
    
    # JWT
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Настройки CORS
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # Пути
    UPLOAD_DIR: str = "./uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    
    # API ключи (будут добавлены позже)
    DEEPSEEK_API_KEY: Optional[str] = None
    HH_RU_CLIENT_ID: Optional[str] = None
    HH_RU_CLIENT_SECRET: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()