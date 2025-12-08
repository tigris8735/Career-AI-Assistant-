from sqlalchemy.orm import Session
from typing import Optional
import uuid
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash


def get_user(db: Session, user_id: uuid.UUID) -> Optional[User]:
    """Получить пользователя по ID"""
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Получить пользователя по email"""
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate) -> User:
    """Создать нового пользователя"""
    hashed_password = get_password_hash(user.password)
    
    db_user = User(
        email=user.email,
        password_hash=hashed_password,
        full_name=user.full_name,
        phone=user.phone,
        language=user.language
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def update_user(db: Session, user_id: uuid.UUID, user_data: dict) -> Optional[User]:
    """Обновить данные пользователя"""
    db_user = get_user(db, user_id)
    
    if not db_user:
        return None
    
    for field, value in user_data.items():
        if hasattr(db_user, field) and value is not None:
            setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    
    return db_user