# План архитектуры системы: AI Career Scout

## 🏗️ Общая архитектурная схема

```
┌─────────────────────────────────────────────────────────────┐
│                   Трехуровневая архитектура                  │
├─────────────────────────────────────────────────────────────┤
│  Уровень 1: Пользовательский интерфейс                      │
│  • Web приложение (Vue 3)                                   │
│  • Мобильное PWA                                            │
│  • Telegram бот                                             │
│  • API для министерств                                      │
└──────────────────────────────┬──────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│        Уровень 2: Бизнес-логика и AI движок                 │
├─────────────────────────────────────────────────────────────┤
│  Сервис тестирования │ Сервис парсинга │ Сервис сопоставления│
│  • Адаптивные тесты  │ • HH.ru парсер  │ • AI матчинг        │
│  • DeepSeek API      │ • Фильтрация    │ • Рекомендации      │
│  • Оценка уровня     │ • Классификация │ • Приоритизация     │
└──────────────────────────────┬──────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│            Уровень 3: Данные и интеграции                   │
├─────────────────────────────────────────────────────────────┤
│  PostgreSQL │ Redis  │ MinIO │ RabbitMQ │ Внешние API       │
│  • Профили  │ • Кэш  │• Файлы│• Очереди │• DeepSeek         │
│  • Результаты│ • Сессии│• Резюме│• Задачи  │• HH.ru          │
│  • Вакансии │ • Тесты│• Логи │• Нотификации│• Министерства  │
└─────────────────────────────────────────────────────────────┘
```

## 📁 Структура проекта

```
ai_career_scout/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── dependencies.py
│   │   │
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── auth/
│   │   │   │   │   ├── routes.py
│   │   │   │   │   └── schemas.py
│   │   │   │   │
│   │   │   │   ├── resumes/
│   │   │   │   │   ├── routes.py
│   │   │   │   │   ├── services.py
│   │   │   │   │   └── parsers.py
│   │   │   │   │
│   │   │   │   ├── testing/
│   │   │   │   │   ├── routes.py
│   │   │   │   │   ├── adapters.py
│   │   │   │   │   └── evaluators.py
│   │   │   │   │
│   │   │   │   ├── vacancies/
│   │   │   │   │   ├── routes.py
│   │   │   │   │   ├── parsers.py
│   │   │   │   │   ├── filters.py
│   │   │   │   │   └── matchers.py
│   │   │   │   │
│   │   │   │   ├── matches/
│   │   │   │   │   ├── routes.py
│   │   │   │   │   └── recommenders.py
│   │   │   │   │
│   │   │   │   └── ministries/
│   │   │   │       ├── federal/
│   │   │   │       │   ├── routes.py
│   │   │   │       │   └── integrations.py
│   │   │   │       │
│   │   │   │       └── moscow/
│   │   │   │           ├── routes.py
│   │   │   │           └── integrations.py
│   │   │   │
│   │   │   └── websocket/
│   │   │       └── testing.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── resume.py
│   │   │   ├── test_result.py
│   │   │   ├── vacancy.py
│   │   │   └── match.py
│   │   │
│   │   ├── services/
│   │   │   ├── deepseek/
│   │   │   │   ├── client.py
│   │   │   │   ├── test_generator.py
│   │   │   │   └── evaluator.py
│   │   │   │
│   │   │   ├── hh_ru/
│   │   │   │   ├── client.py
│   │   │   │   ├── parser.py
│   │   │   │   └── quality_filter.py
│   │   │   │
│   │   │   ├── matching/
│   │   │   │   ├── skill_matcher.py
│   │   │   │   ├── vacancy_ranker.py
│   │   │   │   └── recommender.py
│   │   │   │
│   │   │   └── notification/
│   │   │       ├── email_service.py
│   │   │       ├── telegram_bot.py
│   │   │       └── push_service.py
│   │   │
│   │   └── workers/
│   │       ├── vacancy_parser.py
│   │       ├── test_evaluator.py
│   │       └── match_generator.py
│   │
│   ├── alembic/
│   ├── tests/
│   └── docker-compose.yml
│
├── frontend/
│   ├── src/
│   │   ├── views/
│   │   │   ├── Auth/
│   │   │   │   ├── Login.vue
│   │   │   │   └── Register.vue
│   │   │   │
│   │   │   ├── Dashboard/
│   │   │   │   ├── Overview.vue
│   │   │   │   └── Profile.vue
│   │   │   │
│   │   │   ├── Testing/
│   │   │   │   ├── StartTest.vue
│   │   │   │   ├── TestSession.vue
│   │   │   │   └── Results.vue
│   │   │   │
│   │   │   ├── Vacancies/
│   │   │   │   ├── Search.vue
│   │   │   │   ├── List.vue
│   │   │   │   └── Details.vue
│   │   │   │
│   │   │   ├── Matches/
│   │   │   │   ├── Recommendations.vue
│   │   │   │   ├── Applied.vue
│   │   │   │   └── Statistics.vue
│   │   │   │
│   │   │   └── Ministry/
│   │   │       ├── FederalPortal.vue
│   │   │       └── MoscowPortal.vue
│   │   │
│   │   ├── components/
│   │   │   ├── common/
│   │   │   ├── testing/
│   │   │   └── vacancies/
│   │   │
│   │   ├── composables/
│   │   ├── stores/
│   │   └── router/
│   │
│   ├── public/
│   └── package.json
│
├── mobile-pwa/
│   ├── manifest.json
│   └── service-worker.js
│
├── telegram-bot/
│   ├── bot.py
│   └── handlers/
│
├── ministry-integrations/
│   ├── federal/
│   └── moscow/
│
├── infrastructure/
│   ├── k8s/
│   ├── prometheus/
│   └── nginx/
│
└── docs/
    ├── api/
    ├── user-guides/
    └── integration/
```

## 🔧 Микросервисная архитектура

### Сервис 1: Auth & Profile Service
```python
POST   /api/v1/auth/register        # Регистрация
POST   /api/v1/auth/login           # Вход
POST   /api/v1/auth/refresh         # Обновление токена
GET    /api/v1/profile              # Получить профиль
PUT    /api/v1/profile              # Обновить профиль
POST   /api/v1/resumes              # Загрузить резюме
GET    /api/v1/resumes/{id}         # Получить резюме
```

### Сервис 2: Testing Service
```python
POST   /api/v1/testing/start        # Начать тестирование
GET    /api/v1/testing/{session_id} # Статус теста
POST   /api/v1/testing/{session_id}/answer # Ответить
POST   /api/v1/testing/{session_id}/finish # Завершить
GET    /api/v1/testing/results      # Получить результаты
```

### Сервис 3: Vacancy Service
```python
GET    /api/v1/vacancies/search     # Поиск вакансий
GET    /api/v1/vacancies/{id}       # Детали вакансии
POST   /api/v1/vacancies/sync       # Запустить синхронизацию
GET    /api/v1/vacancies/stats      # Статистика
```

### Сервис 4: Matching Service
```python
POST   /api/v1/matches/generate     # Сгенерировать рекомендации
GET    /api/v1/matches/recommended  # Получить рекомендации
POST   /api/v1/matches/{id}/apply   # Откликнуться на вакансию
GET    /api/v1/matches/status       # Статусы откликов
```

### Сервис 5: Ministry Integration Service
```python
# Федеральное министерство
POST   /api/v1/ministry/federal/bulk-register # Массовая регистрация
GET    /api/v1/ministry/federal/statistics    # Статистика
POST   /api/v1/ministry/federal/reports       # Отчеты

# Московское министерство  
GET    /api/v1/ministry/moscow/vacancies      # Московские вакансии
POST   /api/v1/ministry/moscow/apply-special  # Специальные программы
GET    /api/v1/ministry/moscow/career-centers # Карьерные центры
```

## 🗄️ Модели базы данных

```sql
-- Основные таблицы
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    user_type VARCHAR(50) NOT NULL DEFAULT 'professional',
    ministry_type VARCHAR(50) CHECK (ministry_type IN ('federal', 'moscow', NULL)),
    institute_id VARCHAR(100),
    subscription_tier VARCHAR(50) DEFAULT 'free',
    test_level VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE resumes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    original_filename VARCHAR(500),
    file_path VARCHAR(500),
    file_size INTEGER,
    parsed_data JSONB,
    extracted_skills TEXT[],
    experience_years INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE test_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    test_type VARCHAR(50) NOT NULL,
    questions JSONB NOT NULL,
    answers JSONB,
    score DECIMAL(5,2),
    level_assessment JSONB,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    status VARCHAR(50) DEFAULT 'in_progress'
);

CREATE TABLE vacancies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    hh_id VARCHAR(100) UNIQUE,
    title VARCHAR(500) NOT NULL,
    company_name VARCHAR(255),
    description TEXT,
    requirements JSONB,
    salary_from INTEGER,
    salary_to INTEGER,
    currency VARCHAR(10),
    location VARCHAR(255),
    experience_required VARCHAR(50),
    employment_type VARCHAR(50),
    is_quality BOOLEAN DEFAULT FALSE,
    quality_score DECIMAL(3,2),
    ministry_affiliated BOOLEAN DEFAULT FALSE,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP
);

CREATE TABLE matches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    vacancy_id UUID REFERENCES vacancies(id) ON DELETE CASCADE,
    match_score DECIMAL(5,2) NOT NULL,
    score_breakdown JSONB,
    status VARCHAR(50) DEFAULT 'recommended',
    applied_at TIMESTAMP,
    response_received BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для производительности
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_ministry ON users(ministry_type) WHERE ministry_type IS NOT NULL;
CREATE INDEX idx_vacancies_quality ON vacancies(is_quality, quality_score);
CREATE INDEX idx_vacancies_location ON vacancies(location);
CREATE INDEX idx_matches_user_status ON matches(user_id, status);
CREATE INDEX idx_matches_score ON matches(match_score DESC);
```

## 🔄 Потоки данных

### Стандартный поток соискателя:
```
1. Регистрация → Загрузка резюме → Анализ навыков
2. Адаптивное тестирование → Определение уровня
3. AI-поиск на HH.ru → Фильтрация качества
4. Сопоставление навыков → Топ-10 рекомендаций
5. Выбор вакансий → Автоотклик → Трекинг
```

### Поток студента министерства:
```
1. Массовая регистрация через институт
2. Приоритетный доступ к стажировкам
3. Специальное тестирование с учетом программы
4. Рекомендации от партнерских компаний
5. Отслеживание трудоустройства вендором
```

## 🚀 Стратегия развертывания

### Фаза 1: MVP (1-2 месяца)
- Базовый парсинг HH.ru
- Простое тестирование
- Веб-интерфейс
- 500 тестовых пользователей

### Фаза 2: Расширение (2-4 месяца)
- AI-фильтрация вакансий
- Адаптивное тестирование
- Telegram бот
- Интеграция с 1 министерством

### Фаза 3: Масштабирование (4-6 месяцев)
- Полная интеграция с федеральным и московским министерствами
- Мобильное PWA
- Расширенная аналитика
- 10 000+ активных пользователей
