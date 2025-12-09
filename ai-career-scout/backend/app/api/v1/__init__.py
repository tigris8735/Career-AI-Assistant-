from fastapi import APIRouter
from app.api.v1 import auth

router = APIRouter()

# Подключаем роутеры
router.include_router(auth.router)