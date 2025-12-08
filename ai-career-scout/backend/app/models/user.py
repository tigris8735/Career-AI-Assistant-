from sqlalchemy import Column, String, Integer, DateTime, Enum, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import enum
from app.core.database import Base

class UserTypeEnum(str, enum.Enum):
    STUDENT = "student"
    PROFESSIONAL = "professional"
    MINISTRY_USER = "ministry_user"

class MinistryAffiliationEnum(str, enum.Enum):
    FEDERAL = "federal"
    MOSCOW = "moscow"
    NONE = "none"

class SubscriptionTierEnum(str, enum.Enum):
    FREE = "free"
    STANDARD = "standard"
    PREMIUM = "premium"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255))
    user_type = Column(Enum(UserTypeEnum), default=UserTypeEnum.PROFESSIONAL)
    ministry_affiliation = Column(Enum(MinistryAffiliationEnum), default=MinistryAffiliationEnum.NONE)
    subscription_tier = Column(Enum(SubscriptionTierEnum), default=SubscriptionTierEnum.FREE)
    subscription_data = Column(JSON, default={
        "valid_until": None,
        "features": {
            "resume_analysis": 1,
            "tests_per_month": 10,
            "vacancies_per_day": 5,
            "auto_apply": False
        }
    })
    language = Column(String(10), default="ru")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Связи
    resumes = relationship("Resume", back_populates="user", cascade="all, delete-orphan")
    test_results = relationship("TestResult", back_populates="user", cascade="all, delete-orphan")
    matches = relationship("Match", back_populates="user", cascade="all, delete-orphan")