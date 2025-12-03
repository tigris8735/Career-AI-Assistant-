# Техническая спецификация

## 📋 Общие сведения

**Название проекта:** AI HR Assistant  
**Версия спецификации:** 1.0  
**Дата:** Q1 2024  
**Целевая платформа:** Web (десктоп и мобильные браузеры)  
**Архитектура:** Микросервисная, контейнеризированная

## 🛠️ Технологический стек

### Backend
| Компонент | Технология | Версия | Назначение |
|-----------|------------|---------|------------|
| Основной фреймворк | FastAPI | 0.104+ | REST API |
| Язык программирования | Python | 3.11+ | Бэкенд логика |
| ORM | SQLAlchemy | 2.0+ | Работа с БД |
| Миграции | Alembic | 1.12+ | Миграции схемы БД |
| Аутентификация | JWT |  | Токены доступа |
| Валидация | Pydantic | 2.4+ | Валидация данных |
| Асинхронность | async/await |  | Асинхронные операции |
| HTTP клиент | httpx | 0.25+ | Внешние запросы |
| PDF обработка | PyPDF2 | 3.0+ | Чтение PDF |
| DOCX обработка | python-docx | 0.8+ | Чтение DOCX |

### Frontend
| Компонент | Технология | Версия | Назначение |
|-----------|------------|---------|------------|
| Фреймворк | Vue.js | 3.3+ | SPA приложение |
| Сборщик | Vite | 4.4+ | Сборка проекта |
| UI библиотека | Element Plus | 2.3+ | Компоненты интерфейса |
| State management | Pinia | 2.1+ | Управление состоянием |
| HTTP клиент | Axios | 1.5+ | Запросы к API |
| Роутинг | Vue Router | 4.2+ | Навигация |
| Чарты | Chart.js | 4.3+ | Визуализация данных |
| Экспорт Excel | xlsx | 0.18+ | Генерация Excel |

### Базы данных и хранилища
| Компонент | Технология | Версия | Назначение |
|-----------|------------|---------|------------|
| Основная БД | PostgreSQL | 15+ | Основное хранилище |
| Кэш | Redis | 7.2+ | Сессии, кэширование |
| Файловое хранилище | MinIO | Latest | Хранение файлов |
| Очереди | RabbitMQ | 3.12+ | Асинхронные задачи |

### Инфраструктура
| Компонент | Технология | Версия | Назначение |
|-----------|------------|---------|------------|
| Контейнеризация | Docker | 24.0+ | Контейнеры |
| Оркестрация | Docker Compose | 2.20+ | Локальная разработка |
| CI/CD | GitHub Actions |  | Автоматизация |
| Реверс-прокси | Nginx | 1.24+ | Проксирование |
| Мониторинг | Prometheus | 2.47+ | Метрики |
| Визуализация | Grafana | 10.1+ | Дашборды |
| Логирование | Loki | 2.9+ | Централизованные логи |

## 📊 API Спецификация

### Общие принципы:
- **Базовый URL**: `https://api.hr-assistant.example.com/api/v1`
- **Формат данных**: JSON для всех запросов и ответов
- **Аутентификация**: Bearer JWT токен
- **Коды ответов**: стандартные HTTP коды
- **Версионирование**: в URL пути

### Основные эндпоинты:

#### Аутентификация
```yaml
POST /auth/register:
  summary: Регистрация нового пользователя
  requestBody:
    required: true
    content:
      application/json:
        schema:
          type: object
          properties:
            email:
              type: string
              format: email
            password:
              type: string
              minLength: 8
            full_name:
              type: string
  responses:
    201:
      description: Пользователь создан
    400:
      description: Неверные данные
    409:
      description: Пользователь уже существует

POST /auth/login:
  summary: Вход в систему
  requestBody:
    required: true
    content:
      application/json:
        schema:
          type: object
          properties:
            email:
              type: string
            password:
              type: string
  responses:
    200:
      description: Успешный вход
      content:
        application/json:
          schema:
            type: object
            properties:
              access_token:
                type: string
              refresh_token:
                type: string
              user:
                $ref: '#/components/schemas/User'
    401:
      description: Неверные учетные данные
```

#### Резюме
```yaml
POST /resumes/upload:
  summary: Загрузить резюме
  security:
    - bearerAuth: []
  requestBody:
    required: true
    content:
      multipart/form-data:
        schema:
          type: object
          properties:
            file:
              type: string
              format: binary
            title:
              type: string
            is_primary:
              type: boolean
  responses:
    201:
      description: Резюме загружено
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Resume'
    400:
      description: Неверный формат файла

GET /resumes/{resume_id}:
  summary: Получить резюме по ID
  security:
    - bearerAuth: []
  parameters:
    - name: resume_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
  responses:
    200:
      description: Данные резюме
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Resume'
    404:
      description: Резюме не найдено
```

## 🗄️ Модели данных

### User (Пользователь)
```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255))
    phone = Column(String(50))
    location = Column(String(255))
    subscription_tier = Column(String(50), default="free")
    subscription_ends_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    resumes = relationship("Resume", back_populates="user")
    applications = relationship("Application", back_populates="user")
```

### Resume (Резюме)
```python
class Resume(Base):
    __tablename__ = "resumes"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    title = Column(String(255))
    original_filename = Column(String(500))
    file_path = Column(String(500))
    file_size = Column(Integer)
    file_type = Column(String(50))
    
    # Парсированные данные
    parsed_data = Column(JSONB)
    raw_text = Column(Text)
    
    # Извлеченные поля
    full_name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    experience_years = Column(Integer)
    skills = Column(ARRAY(String))
    education = Column(JSONB)
    work_experience = Column(JSONB)
    
    # Флаги
    is_primary = Column(Boolean, default=False)
    is_public = Column(Boolean, default=False)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="resumes")
    matches = relationship("MatchResult", back_populates="resume")
```

## 🔐 Безопасность

### Аутентификация
- JWT токены с expiry 24 часа
- Refresh токены с expiry 30 дней
- Хэширование паролей с bcrypt

### Авторизация
- Ролевая модель: user, premium_user, admin
- Права доступа к ресурсам
- Проверка владения ресурсом

### Защита данных
- HTTPS для всех соединений
- Шифрование чувствительных данных в БД
- Регулярные security аудиты
- Защита от инъекций и XSS

### Лимиты запросов
```python
# Rate limiting конфигурация
RATE_LIMITS = {
    "anonymous": "100/hour",
    "authenticated": "1000/hour",
    "premium": "5000/hour",
    "admin": "10000/hour"
}
```
