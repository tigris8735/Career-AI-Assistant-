# backend/app/models/__init__.py
from app.models.user import User
from app.models.resume import Resume
from app.models.test_result import TestResult
from app.models.vacancy import Vacancy
from app.models.match import Match
from app.models.subscription import Subscription

__all__ = ['User', 'Resume', 'TestResult', 'Vacancy', 'Match', 'Subscription']