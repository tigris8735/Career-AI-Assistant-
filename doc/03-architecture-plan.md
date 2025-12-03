# План архитектуры системы

## 🏗️ Общая архитектурная схема

```
┌─────────────────────────────────────────────────────────────┐
│                    Клиентские приложения                    │
├─────────────────────────────────────────────────────────────┤
│  Веб-интерфейс (Vue.js)   │   Мобильное приложение (React  │
│                           │   Native - в будущем)          │
└──────────────┬────────────┴──────────────┬─────────────────┘
               │                           │
               ▼                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  API Gateway / Load Balancer                 │
│                    (Nginx / Traefik)                        │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
    ┌──────────────────────────────────────────────────┐
    │               Микросервисный слой                │
    ├──────────┬──────────┬──────────┬─────────────────┤
    │   User   │ Resume   │ Vacancy  │ Matching        │
    │ Service  │ Service  │ Service  │ Service         │
    └──────────┴──────────┴──────────┴─────────────────┘
              │           │          │           │
              ▼           ▼          ▼           ▼
    ┌──────────────────────────────────────────────────┐
    │               Общие сервисы                      │
    ├──────────┬──────────┬──────────┬─────────────────┤
    │   Auth   │   File   │   LLM    │   Queue         │
    │ Service  │ Storage  │ Gateway  │   Manager       │
    └──────────┴──────────┴──────────┴─────────────────┘
              │           │          │           │
              ▼           ▼          ▼           ▼
    ┌──────────────────────────────────────────────────┐
    │              Инфраструктурный слой               │
    ├──────────┬──────────┬──────────┬─────────────────┤
    │   PostgreSQL │   Redis   │   MinIO   │   RabbitMQ  │
    │   (основная │   (кэш,    │   (файлы) │   (очереди) │
    │     БД)     │  сессии)   │           │             │
    └──────────┴──────────┴──────────┴─────────────────┘
              │           │          │           │
              ▼           ▼          ▼           ▼
    ┌──────────────────────────────────────────────────┐
    │             Внешние интеграции                   │
    ├──────────┬──────────┬──────────┬─────────────────┤
    │  HH.ru   │  OpenAI/ │ Payment  │ Email/SMS       │
    │   API    │  Yandex  │ Gateway  │  Services       │
    │          │   GPT    │          │                 │
    └──────────┴──────────┴──────────┴─────────────────┘
```

## 📁 Структура проекта

### Корневая структура
```
hr_assistant_web/
│
├── backend/                    # FastAPI сервер (Разработчик)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # Точка входа FastAPI
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints.py  # Все эндпоинты
│   │   │   └── dependencies.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py     # Конфигурация
│   │   │   └── security.py   # CORS, аутентификация
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── database.py   # SQLAlchemy модели
│   │   │   └── schemas.py    # Pydantic схемы
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── file_service.py    # Обработка PDF/DOCX
│   │   │   ├── llm_service.py     # Взаимодействие с удаленной LLM
│   │   │   ├── matching_service.py # Сопоставление вакансий
│   │   │   └── export_service.py   # Экспорт в Excel
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   └── session.py    # Подключение к БД
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── validators.py
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/                  # Веб-интерфейс (Разработчик)
│   ├── public/
│   │   ├── index.html        # Основной HTML
│   │   ├── favicon.ico
│   │   └── assets/
│   ├── src/
│   │   ├── components/
│   │   │   ├── VacancyTable.vue  # Таблица вакансий
│   │   │   ├── UploadForm.vue    # Форма загрузки
│   │   │   ├── ExportButton.vue  # Кнопка экспорта
│   │   │   └── CandidateCard.vue # Карточка кандидата
│   │   ├── views/
│   │   │   ├── Dashboard.vue     # Главная страница
│   │   │   ├── Vacancies.vue     # Страница вакансий
│   │   │   └── Upload.vue        # Страница загрузки
│   │   ├── services/
│   │   │   ├── api.js        # Клиент для API
│   │   │   └── excel.js      # Экспорт в Excel
│   │   ├── store/            # Pinia/Vuex хранилище
│   │   │   └── index.js
│   │   ├── App.vue
│   │   └── main.js
│   ├── package.json
│   ├── vite.config.js        # или webpack.config.js
│   ├── Dockerfile
│   └── .env.example
│
├── ml_pipeline/              # Парадигма и промпты (Человек_2)
│   ├── __init__.py
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── resume_analysis.json     # Промпты для анализа резюме
│   │   ├── vacancy_matching.json    # Промпты для сопоставления
│   │   ├── summary_generation.json  # Промпты для summary
│   │   └── skill_extraction.json    # Промпты для извлечения навыков
│   ├── templates/
│   │   ├── resume_template.md       # Шаблон структуры резюме
│   │   └── vacancy_template.md      # Шаблон структуры вакансии
│   ├── processors/
│   │   ├── __init__.py
│   │   ├── text_extractor.py        # Извлечение текста из PDF/DOCX
│   │   └── data_formatter.py        # Форматирование данных для LLM
│   └── README.md
│
├── docs/                     # Документация (Человек_3)
│   ├── api/
│   │   ├── endpoints.md     # Документация API
│   │   └── examples.md      # Примеры запросов
│   ├── deployment/
│   │   ├── backend.md       # Развертывание бэкенда
│   │   ├── frontend.md      # Развертывание фронтенда
│   │   └── hosting.md       # Бесплатные хостинги
│   ├── user-guide/
│   │   ├── quick-start.md   # Быстрый старт
│   │   └── features.md      # Описание возможностей
│   └── ml-pipeline/
│       ├── prompts-guide.md # Руководство по промптам
│       └── integration.md   # Интеграция с LLM
│
├── nginx/                    # Конфигурация nginx
│   ├── nginx.conf
│   └── ssl/                  # SSL сертификаты (если нужно)
│
├── docker-compose.yml        # Docker Compose
├── .env.example              # Пример переменных окружения
├── .gitignore
├── README.md                 # Общая документация
└── Makefile                  # Скрипты для удобства
```

## 🔧 Компоненты системы

### 1. Backend (FastAPI)

#### Основные модули:
- **`main.py`** - точка входа, инициализация приложения
- **`endpoints.py`** - REST API эндпоинты
- **`services/`** - бизнес-логика в отдельных сервисах

#### Эндпоинты API:
```python
# Основные маршруты
POST   /api/v1/auth/register      # Регистрация
POST   /api/v1/auth/login         # Авторизация
POST   /api/v1/auth/refresh       # Обновление токена

POST   /api/v1/resumes/upload     # Загрузка резюме
GET    /api/v1/resumes/{id}       # Получить резюме
DELETE /api/v1/resumes/{id}       # Удалить резюме

GET    /api/v1/vacancies/search   # Поиск вакансий
GET    /api/v1/vacancies/{id}     # Детали вакансии
POST   /api/v1/vacancies/match    # Сопоставление с резюме

GET    /api/v1/matches            # Результаты сопоставления
POST   /api/v1/applications       # Отправить отклик
GET    /api/v1/analytics          # Аналитика

POST   /api/v1/chat/message       # Отправить сообщение в чат
GET    /api/v1/chat/history       # История чата
```

### 2. Frontend (Vue.js)

#### Структура компонентов:
```
src/
├── views/
│   ├── Dashboard.vue           # Главная страница
│   ├── Login.vue              # Страница входа
│   ├── Register.vue           # Страница регистрации
│   ├── ResumeUpload.vue       # Загрузка резюме
│   ├── VacancySearch.vue      # Поиск вакансий
│   ├── MatchResults.vue       # Результаты сопоставления
│   ├── ChatAssistant.vue      # Чат с AI
│   └── Settings.vue           # Настройки
├── components/
│   ├── common/
│   │   ├── Header.vue
│   │   ├── Footer.vue
│   │   ├── Sidebar.vue
│   │   └── Loader.vue
│   ├── resume/
│   │   ├── UploadForm.vue
│   │   ├── ResumeCard.vue
│   │   └── SkillsChart.vue
│   ├── vacancies/
│   │   ├── VacancyCard.vue
│   │   ├── FilterPanel.vue
│   │   └── VacancyTable.vue
│   └── chat/
│       ├── ChatWindow.vue
│       ├── MessageBubble.vue
│       └── TypingIndicator.vue
└── store/
    ├── auth.js               # Хранилище авторизации
    ├── resume.js             # Хранилище резюме
    ├── vacancies.js          # Хранилище вакансий
    └── chat.js               # Хранилище чата
```

### 3. ML Pipeline

#### Промпты для LLM:
```json
// ml_pipeline/prompts/resume_analysis.json
{
  "system": "Ты профессиональный HR-аналитик с 10-летним опытом. Твоя задача — анализировать резюме и извлекать структурированные данные.",
  "user_template": "Проанализируй следующий текст резюме и извлеки:\n\n1. Личная информация (имя, контакты, локация)\n2. Опыт работы (компании, должности, периоды, обязанности)\n3. Образование (учреждения, специальности, годы)\n4. Навыки (технические и soft skills)\n5. Достижения и проекты\n\nТекст резюме:\n{resume_text}",
  "output_format": {
    "type": "json",
    "schema": {
      "personal_info": {
        "name": "string",
        "email": "string",
        "phone": "string",
        "location": "string"
      },
      "experience": [
        {
          "company": "string",
          "position": "string",
          "period": "string",
          "responsibilities": "array[string]"
        }
      ],
      "skills": {
        "technical": "array[string]",
        "soft": "array[string]"
      }
    }
  }
}
```

### 4. База данных

#### Схема PostgreSQL:
```sql
-- Пользователи
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    subscription_tier VARCHAR(50) DEFAULT 'free',
    subscription_ends_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Резюме
CREATE TABLE resumes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    original_filename VARCHAR(255),
    file_path VARCHAR(500),
    parsed_data JSONB,
    skills TEXT[],
    experience_years INTEGER,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Вакансии
CREATE TABLE vacancies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    hh_id VARCHAR(100) UNIQUE,
    title VARCHAR(500) NOT NULL,
    company VARCHAR(255),
    salary_from INTEGER,
    salary_to INTEGER,
    currency VARCHAR(10),
    experience_required VARCHAR(100),
    employment_type VARCHAR(50),
    skills TEXT[],
    requirements JSONB,
    url TEXT,
    parsed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    indexed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Результаты сопоставления
CREATE TABLE match_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    resume_id UUID REFERENCES resumes(id) ON DELETE CASCADE,
    vacancy_id UUID REFERENCES vacancies(id) ON DELETE CASCADE,
    match_score DECIMAL(5,2),
    score_details JSONB,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(resume_id, vacancy_id)
);
```

## 🌐 Сетевая архитектура

### Продакшен окружение:
```
┌─────────────────────────────────────────────────────────────┐
│                     Пользовательский браузер                │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                       Cloudflare CDN                        │
│                     (DDoS защита, кэш)                      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     Load Balancer (Nginx)                   │
└──────────────┬──────────────┬──────────────┬────────────────┘
               │              │              │
               ▼              ▼              ▼
┌──────────────┴─────┐┌───────┴──────┐┌───────┴──────┐
│  Frontend Server 1 ││Frontend Svr 2││Frontend Svr 3│
│   (Vue.js - SPA)   ││   (Vue.js)   ││   (Vue.js)   │
└──────────┬─────────┘└───────┬──────┘└───────┬──────┘
           │                  │                │
           └──────────────────┼────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     API Gateway (Kong)                      │
└──────────────┬──────────────┬──────────────┬────────────────┘
               │              │              │
               ▼              ▼              ▼
┌──────────────┴─────┐┌───────┴──────┐┌───────┴──────┐
│   Backend Svr 1    ││ Backend Svr 2 ││ Backend Svr 3 │
│   (FastAPI)        ││  (FastAPI)    ││  (FastAPI)    │
└──────────┬─────────┘└───────┬──────┘└───────┬──────┘
           │                  │                │
           └──────────────────┼────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Сервисы данных                           │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│PostgreSQL│  Redis   │  MinIO   │RabbitMQ  │   Мониторинг    │
│  Primary │ (Кэш)    │ (Файлы)  │(Очереди) │(Prometheus,     │
│  + Replica│         │          │          │   Grafana)      │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘
```

## 🔄 Потоки данных

### 1. Процесс загрузки и анализа резюме:
```
Пользователь → Загружает файл → Бэкенд → 
→ Сохраняет в MinIO → Извлекает текст → 
→ Отправляет в LLM → Получает структурированные данные → 
→ Сохраняет в PostgreSQL → Возвращает результат пользователю
```

### 2. Процесс поиска и сопоставления вакансий:
```
Пользователь → Запускает поиск → Бэкенд → 
→ Запрашивает HH.ru API → Сохраняет вакансии → 
→ Запускает Matching Service → Рассчитывает score → 
→ Ранжирует результаты → Возвращает пользователю
```

### 3. Процесс автоматического отклика:
```
Система → Выбирает вакансию → Генерирует адаптированное резюме → 
→ Создает сопроводительное письмо → Использует "умного клиента" → 
→ Имитирует поведение человека → Отправляет отклик → 
→ Сохраняет статус → Уведомляет пользователя
```

## 🚀 Стратегия развертывания

### Этап 1: Локальная разработка
- Docker Compose для всех сервисов
- SQLite для разработки
- Mock внешних API

### Этап 2: Staging окружение
- Отдельный сервер/контейнеры
- Тестовые данные
- Полная интеграция с API

### Этап 3: Продакшен
- Kubernetes кластер
- Автоматическое масштабирование
- Гео-репликация данных
- Резервное копирование

## 📈 Мониторинг и логирование

### Метрики для мониторинга:
1. **Системные метрики**: CPU, RAM, Disk, Network
2. **Бизнес метрики**: активные пользователи, загрузки, отклики
3. **Производительность**: время ответа API, ошибки
4. **Интеграции**: статус внешних сервисов

### Логирование:
- Структурированные логи в JSON формате
- Централизованное хранение (ELK/ Loki)
- Алертинг при ошибках (Telegram/Slack/Email)

