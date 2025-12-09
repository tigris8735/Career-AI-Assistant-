# Импортируем все модели
from app.models.user import User
from app.models.resume import Resume
from app.models.vacancy import Vacancy
from app.models.test_result import TestResult
from app.models.match import Match

__all__ = [
    "User",
    "Resume", 
    "Vacancy",
    "TestResult",
    "Match"
]