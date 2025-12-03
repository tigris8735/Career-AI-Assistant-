# AI HR Assistant - Документация проекта

![Project Status](https://img.shields.io/badge/status-mvp_ready-green)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 📖 Оглавление

1. [Введение](#-введение)
2. [Быстрый старт](#-быстрый-старт)
3. [Архитектура](#-архитектура)
4. [Документация по модулям](#-документация-по-модулям)
5. [Развертывание](#-развертывание)
6. [Разработка](#-разработка)
7. [Тестирование](#-тестирование)

## 🎯 Введение

**AI HR Assistant** — это интеллектуальный сервис автоматизации поиска работы, который помогает соискателям находить подходящие вакансии, адаптировать резюме и готовиться к собеседованиям с помощью искусственного интеллекта.

### Ключевые возможности:
- 📄 **Анализ резюме** - автоматическое извлечение и структурирование данных из PDF/DOCX
- 🔍 **Поиск вакансий** - интеграция с HH.ru и другими платформами
- 🤝 **Сопоставление** - алгоритмы matching резюме с вакансиями
- ✍️ **Генерация резюме** - адаптация под конкретные вакансии
- 🤖 **AI-чат** - подготовка к собеседованиям и ответы на вопросы
- ⚡ **Автоматизация** - умные отклики и управление кампаниями

## 🚀 Быстрый старт

### Требования к окружению:
- Docker 20.10+
- Docker Compose 2.20+
- 4GB RAM минимум
- 10GB свободного места

### Локальный запуск за 5 минут:

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/your-org/hr-assistant.git
cd hr-assistant
```

2. **Настройте переменные окружения:**
```bash
cp .env.example .env
# Отредактируйте .env файл, добавьте свои API ключи
```

3. **Запустите приложение:**
```bash
docker-compose up -d
```

4. **Откройте в браузере:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API документация: http://localhost:8000/docs

## 🏗️ Архитектура

### Общая схема:
```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Frontend      │────▶│   API Gateway   │────▶│   Backend       │
│   (Vue.js SPA)  │     │   (Nginx)       │     │   (FastAPI)     │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
           ┌─────────────────────────────────────────────┘
           │
    ┌──────▼──────┐     ┌──────────────┐     ┌──────────────┐
    │   Services   │────▶│   Database   │────▶│   External   │
    │   Layer      │     │   Layer      │     │   Services   │
    └──────────────┘     └──────────────┘     └──────────────┘
```

### Технологический стек:
| Компонент | Технологии |
|-----------|------------|
| **Frontend** | Vue.js 3, Vite, Pinia, Element Plus |
| **Backend** | Python 3.11, FastAPI, SQLAlchemy, Pydantic |
| **Базы данных** | PostgreSQL, Redis |
| **Хранилище** | MinIO/S3 |
| **Очереди** | Celery, RabbitMQ |
| **ML/AI** | OpenAI API, Yandex GPT, Custom models |
| **Инфраструктура** | Docker, Docker Compose, Nginx |

## 📚 Документация по модулям

### Основная документация:

| Документ | Назначение | Статус |
|----------|------------|--------|
| [📋 Бизнес-требования](01-business-requirements.md) | Бизнес-цели, рынок, монетизация | ✅ Завершен |
| [🔧 Системный анализ](02-system-analysis.md) | Функциональные и нефункциональные требования | ✅ Завершен |
| [🏗️ Архитектура](03-architecture-plan.md) | Техническая архитектура и структура проекта | ✅ Завершен |
| [⚙️ Техническая спецификация](04-technical-specification.md) | Детальные технические требования и API | ✅ Завершен |
| [🧪 План тестирования](05-testing-plan.md) | Стратегия и сценарии тестирования | ✅ Завершен |
| [✅ Отчет приемки](06-project-acceptance-report.md) | Результаты приемки проекта | ✅ Завершен |

## 🚢 Развертывание

### Локальная разработка:
```bash
# Клонирование и настройка
git clone <repo-url>
cd hr-assistant
cp .env.example .env
# Редактируем .env файл

# Запуск всех сервисов
docker-compose up -d

# Проверка статуса
docker-compose ps

# Логи
docker-compose logs -f backend
```

### Продакшен развертывание:
```bash
# Используем продакшен конфигурацию
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Миграции базы данных
docker-compose exec backend alembic upgrade head

# Сбор статики фронтенда
docker-compose exec frontend npm run build
```

## 💻 Разработка

### Установка для разработки:

#### Backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements/dev.txt

# Запуск в режиме разработки
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend:
```bash
cd frontend
npm install

# Запуск в режиме разработки
npm run dev
```

## 🧪 Тестирование

### Запуск тестов:
```bash
# Все тесты
make test

# Только unit тесты
make test-unit

# Только интеграционные тесты
make test-integration

# E2E тесты
make test-e2e
```

### Code quality:
```bash
# Линтинг
make lint

# Форматирование
make format

# Проверка типов
make type-check

# Security audit
make security-scan
```



## 📁 **Структура директории docs/:**

```

docs/
├── 📄 01-business-requirements.md         # Бизнес-цели, рынок, монетизация
├── 📄 02-system-analysis.md               # Функциональные требования
├── 📄 03-architecture-plan.md             # Техническая архитектура
├── 📄 04-technical-specification.md       # Детальные технические требования
├── 📄 05-testing-plan.md                  # План тестирования
└── 📄 README.md                           # Общая документация проекта

```