# Career AI Assistant - Документация проекта

![Project Status](https://img.shields.io/badge/status-development-yellow)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-dual_sided-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 📖 Оглавление

1. [Введение](#-введение)
2. [Для кого этот продукт](#-для-кого-этот-продукт)
3. [Быстрый старт](#-быстрый-старт)
4. [Архитектура](#-архитектура)
5. [Документация по модулям](#-документация-по-модулям)
6. [Для разработчиков](#-для-разработчиков)
7. [Контакты и поддержка](#-контакты-и-поддержка)

## 🎯 Введение

**Career AI Assistant** — это интеллектуальная двусторонняя платформа, которая помогает **соискателям** найти работу мечты и **компаниям** — находить идеальных кандидатов с помощью искусственного интеллекта.

### 🌟 Двойная ценность

#### Для соискателей:
- 🤖 **Персональный AI-помощник** для поиска работы
- 📄 **Умный анализ резюме** с рекомендациями по улучшению
- 🔍 **Интеллектуальный поиск** вакансий по тысячам предложений
- 🎯 **Автоматическая адаптация** резюме под каждую вакансию
- 💬 **AI-симулятор собеседований** с реалистичной подготовкой
- 📊 **Аналитика прогресса** и персональные рекомендации

#### Для HR и компаний:
- ⚡ **Ускоренный подбор** кандидатов с AI-фильтрацией
- 🎯 **Точное ранжирование** резюме по релевантности
- 📈 **Глубокая аналитика** навыков и компетенций
- 🤖 **Автоматизация рутины** — рассылки, отклики, уведомления
- 📊 **Прогноз успешности** найма на основе данных
- 🔄 **Интеграция** с HH.ru, LinkedIn и ATS системами

### 🎯 Ключевые отличия

| Особенность | Career AI Assistant | Традиционные сервисы |
|------------|-------------------|---------------------|
| **AI-анализ резюме** | Глубокая аналитика с рекомендациями | Базовый парсинг |
| **Автоматическая адаптация** | Резюме под каждую вакансию | Статическое резюме |
| **Интеллектуальный поиск** | Semantic search + рекомендации | Ключевые слова |
| **Прогноз успеха** | AI предсказывает успешность найма | Нет прогнозов |
| **Двусторонняя платформа** | Для соискателей И компаний | Обычно только для одной стороны |

## 👥 Для кого этот продукт

### 👨‍💻 Для соискателей:
- **Активно ищущие работу** — хотите найти её быстрее
- **Пассивные соискатели** — открыты к предложениям
- **IT-специалисты** — разработчики, аналитики, DevOps
- **Менеджеры и руководители** — project managers, team leads
- **Выпускники вузов** — начинающие специалисты
- **Специалисты в переходе** — меняющие профессию или индустрию

### 🏢 Для компаний и HR:
- **Корпоративные HR-отделы** — ускорение процессов подбора
- **Рекрутинговые агентства** — повышение эффективности работы
- **Стартапы и малый бизнес** — нет выделенного HR
- **HR-фрилансеры** — независимые рекрутеры
- **Технические рекрутеры** — поиск IT-специалистов
- **Кадровые службы** — автоматизация рутинных задач

## 🚀 Быстрый старт

### Требования к окружению:
- Docker 20.10+
- Docker Compose 2.20+
- 4GB RAM минимум
- 10GB свободного места

### Локальный запуск за 5 минут:

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/your-org/career-ai-assistant.git
cd career-ai-assistant
```

2. **Настройте переменные окружения:**
```bash
cp .env.example .env
# Отредактируйте .env файл, добавьте API ключи
```

3. **Запустите приложение:**
```bash
docker-compose up -d
```

4. **Откройте в браузере:**
- **Лендинг:** http://localhost:3000
- **Для соискателей:** http://localhost:3001
- **Для HR/компаний:** http://localhost:3002
- **API документация:** http://localhost:8000/docs

5. **Создайте тестовых пользователей:**
```bash
# Создать соискателя
curl -X POST http://localhost:8000/api/v1/seekers/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "seeker@test.com", "password": "Test123!", "full_name": "Иван Иванов"}'

# Создать компанию
curl -X POST http://localhost:8000/api/v1/hr/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "hr@company.com", "password": "Test123!", "company_name": "Технологии Будущего"}'
```

## 🏗️ Архитектура

### Общая схема:
```
┌─────────────────────────────────────────────────────────────┐
│              Двусторонняя архитектура                       │
├─────────────────────────────────────────────────────────────┤
│  Соискатели                         HR/Компании              │
│  • Анализ резюме                    • Анализ кандидатов     │
│  • Поиск вакансий                   • Управление вакансиями │
│  • AI-подготовка                    • Автоматизация отбора  │
│  • Автоотклики                      • Аналитика подбора     │
└──────────────┬──────────────────────┬──────────────┬────────┘
               │                      │              │
               ▼                      ▼              ▼
┌─────────────────────────────────────────────────────────────┐
│                  Общий AI-движок и инфраструктура            │
│        (Раздельные API, общие сервисы, единая БД)           │
└─────────────────────────────────────────────────────────────┘
               │                      │              │
               ▼                      ▼              ▼
┌──────────────┴──────┐    ┌──────────┴──────┐    ┌─┴──────────┐
│  Внешние интеграции │    │   Базы данных   │    │   Очереди  │
│  • HH.ru            │    │  • PostgreSQL   │    │  • RabbitMQ│
│  • LinkedIn         │    │  • Redis        │    │  • Celery  │
│  • Платежные системы│    │  • MinIO/S3     │    └────────────┘
└─────────────────────┘    └─────────────────┘
```

### Технологический стек:

#### Backend:
- **Язык:** Python 3.11+
- **Фреймворк:** FastAPI (асинхронный)
- **Базы данных:** PostgreSQL 15, Redis 7
- **Очереди:** Celery + RabbitMQ
- **Файловое хранилище:** MinIO / S3 совместимое
- **ML/Аналитика:** scikit-learn, spaCy, трансформеры

#### Frontend:
- **Фреймворк:** Vue.js 3 + Composition API
- **Билд:** Vite
- **UI библиотеки:** 
  - Для соискателей: Element Plus
  - Для HR: Ant Design Vue
- **State management:** Pinia
- **Роутинг:** Vue Router 4

#### DevOps:
- **Контейнеризация:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Мониторинг:** Prometheus + Grafana + Loki
- **Логирование:** Structured JSON logs
- **Хостинг:** Kubernetes (продакшен)

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

### Дополнительная документация:

#### Для пользователей:
- [Руководство соискателя](user-guides/seeker-guide.md) - как использовать платформу для поиска работы
- [Руководство HR](user-guides/hr-guide.md) - как использовать платформу для подбора
- [FAQ](user-guides/faq.md) - ответы на частые вопросы
- [Тарифы и цены](user-guides/pricing.md) - информация о подписках

#### Для разработчиков:
- [API документация](api/overview.md) - полная спецификация API
- [Интеграции](api/integrations.md) - интеграция с внешними сервисами
- [Развертывание](deployment/overview.md) - инструкции по деплою
- [Контрибьютинг](development/contributing.md) - руководство для контрибьюторов

#### Для ML/Data Science:
- [ML Pipeline](ml-pipeline/overview.md) - архитектура ML компонентов
- [Модели](ml-pipeline/models.md) - описание используемых моделей
- [Данные](ml-pipeline/data.md) - структура данных и датасетов

## 💻 Для разработчиков

### Установка для разработки:

#### 1. Клонирование и настройка:
```bash
git clone https://github.com/your-org/career-ai-assistant.git
cd career-ai-assistant
cp .env.example .env.development
# Настройте переменные окружения
```

#### 2. Запуск бэкенда:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements/dev.txt

# Запуск в режиме разработки
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### 3. Запуск фронтенда:
```bash
# Для соискателей
cd frontend/seekers
npm install
npm run dev

# Для HR
cd frontend/hr
npm install
npm run dev

# Лендинг
cd frontend/landing
npm install
npm run dev
```

### Структура проекта:
```
career-ai-assistant/
├── backend/                    # Основной бэкенд
│   ├── app/
│   │   ├── api/seekers/       # API для соискателей
│   │   ├── api/hr/            # API для HR
│   │   ├── models/            # Модели данных
│   │   ├── services/          # Бизнес-логика
│   │   └── utils/             # Вспомогательные функции
│   ├── tests/                 # Тесты
│   ├── migrations/            # Миграции БД
│   └── requirements/          # Зависимости
│
├── frontend/                  # Фронтенд приложения
│   ├── seekers/              # Приложение для соискателей
│   ├── hr/                   # Приложение для HR
│   └── landing/              # Маркетинговый лендинг
│
├── ml_pipeline/              # ML модели и AI
│   ├── models/               # Модели машинного обучения
│   ├── training/             # Обучение моделей
│   └── deployment/           # Деплой ML
│
├── docs/                     # Документация
│   ├── api/                  # API документация
│   ├── user-guides/          # Руководства пользователей
│   ├── deployment/           # Деплоймент
│   └── development/          # Разработка
│
├── docker-compose.yml        # Docker Compose конфигурация
├── .env.example              # Пример переменных окружения
├── .gitignore               # Git ignore файл
├── README.md                # Основной README
└── Makefile                 # Скрипты для удобства
```

### Рабочий процесс:
1. **Создайте ветку:** `git checkout -b feature/your-feature-name`
2. **Разработайте фичу:** Следуйте кодстайлу проекта
3. **Добавьте тесты:** Для новой функциональности
4. **Запустите тесты:** `make test`
5. **Создайте PR:** В ветку `develop`
6. **Code review:** После ревью - мердж в `develop`
7. **Релиз:** Из `develop` в `main` через теги

## 🧪 Тестирование

### Команды для тестирования:
```bash
# Все тесты
make test

# Специфичные тесты
make test-unit          # Юнит тесты
make test-integration   # Интеграционные тесты
make test-e2e           # End-to-end тесты
make test-coverage      # Тесты с покрытием

# Code quality
make lint               # Линтинг
make format             # Форматирование кода
make type-check         # Проверка типов
make security-scan      # Security аудит
```

### Нагрузочное тестирование:
```bash
# Запуск k6 тестов
make load-test

# Запуск специфичных сценариев
make load-test-seekers   # Тестирование нагрузки соискателей
make load-test-hr        # Тестирование нагрузки HR
```

## 📊 Мониторинг

### Доступные инструменты:
- **Prometheus:** http://localhost:9090 (метрики)
- **Grafana:** http://localhost:3003 (дашборды)
- **Loki:** http://localhost:3100 (логи)
- **MinIO Console:** http://localhost:9001 (файлы)

### Ключевые метрики:

#### Для соискателей:
- Время анализа резюме
- Конверсия регистраций
- Успешность откликов
- Удовлетворенность AI-чатом

#### Для HR:
- Время обработки резюме
- Качество AI рекомендаций
- Retention клиентов
- Эффективность найма

#### Системные:
- Uptime > 99.5%
- API response time p95 < 2s
- Ошибки < 1%
- Использование ресурсов

## 📞 Контакты и поддержка

### Команда проекта:
| Роль | Контакт | Ответственность |
|------|---------|-----------------|
| **Product Owner** | Алексей Иванов - a.ivanov@company.com | Стратегия, roadmap |
| **CTO** | Дмитрий Петров - d.petrov@company.com | Техническая архитектура |
| **Backend Lead** | Сергей Сидоров - s.sidorov@company.com | Бэкенд разработка |
| **Frontend Lead** | Мария Кузнецова - m.kuznetsova@company.com | Фронтенд разработка |
| **ML Engineer** | Иван Смирнов - i.smirnov@company.com | AI/ML компоненты |
| **QA Lead** | Анна Волкова - a.volkova@company.com | Тестирование, качество |

### Полезные ссылки:
- **Репозиторий:** https://github.com/your-org/career-ai-assistant
- **Документация:** https://docs.career-ai.com
- **Продакшен:** https://app.career-ai.com (соискатели), https://hr.career-ai.com (HR)
- **Лендинг:** https://career-ai.com
- **Статус системы:** https://status.career-ai.com
- **Блог:** https://blog.career-ai.com
- **Поддержка:** support@career-ai.com

### Сообщество:
- [Discord](https://discord.gg/career-ai) - чат разработчиков и пользователей
- [Telegram канал](https://t.me/career_ai_news) - новости и обновления
- [GitHub Discussions](https://github.com/your-org/career-ai-assistant/discussions) - обсуждения
- [Stack Overflow](https://stackoverflow.com/questions/tagged/career-ai-assistant) - вопросы и ответы

## 📄 Лицензия

Этот проект лицензирован под лицензией MIT - смотрите файл [LICENSE](LICENSE) для деталей.

## 🙏 Благодарности

- Команде **HH.ru** за предоставление API для интеграции
- **OpenAI** и другим провайдерам LLM за AI модели
- Сообществу **open-source** за все используемые библиотеки и инструменты
- Нашим **бета-тестерам** за ценные отзывы и предложения
- Всем **контрибьюторам**, которые помогают улучшать проект

## 🚀 Наша миссия

Мы верим, что каждый человек заслуживает работу, которая приносит удовлетворение, и каждая компания — команду, которая верит в общее дело. Career AI Assistant создан, чтобы сделать процесс поиска работы и подбора персонала более человечным, эффективным и справедливым с помощью технологий.

---

*Последнее обновление: 20 января 2024*  
*Версия документации: 1.0.0*  
*© 2024 Career AI Assistant Team. Все права защищены.*
```

## 📁 **Файл 4: docs/04-technical-specification.md**

```markdown
# Техническая спецификация

## 📋 Общие сведения

**Название проекта:** Career AI Assistant  
**Версия спецификации:** 1.0  
**Дата:** Q1 2024  
**Тип:** Двусторонняя веб-платформа  
**Архитектура:** Микросервисная, контейнеризированная  
**Целевые пользователи:** Соискатели (Seekers) и HR-специалисты

## 🛠️ Технологический стек

### Backend
| Компонент | Технология | Версия | Назначение |
|-----------|------------|---------|------------|
| Основной фреймворк | FastAPI | 0.104+ | REST API для обоих пользовательских типов |
| Язык программирования | Python | 3.11+ | Бэкенд логика, ML модели |
| ORM | SQLAlchemy | 2.0+ | Работа с БД |
| Миграции | Alembic | 1.12+ | Миграции схемы БД |
| Аутентификация | JWT + OAuth2 |  | Раздельная аутентификация для seeker/HR |
| Валидация | Pydantic | 2.4+ | Валидация данных |
| Асинхронность | async/await |  | Асинхронные операции |
| HTTP клиент | httpx | 0.25+ | Внешние запросы |
| PDF обработка | PyPDF2 | 3.0+ | Чтение PDF |
| DOCX обработка | python-docx | 0.8+ | Чтение DOCX |
| NLP библиотеки | spaCy | 3.7+ | Обработка естественного языка |
| ML фреймворки | scikit-learn | 1.3+ | Машинное обучение |

### Frontend
| Компонент | Технология | Версия | Назначение |
|-----------|------------|---------|------------|
| Основной фреймворк | Vue.js | 3.3+ | SPA приложения |
| Сборщик | Vite | 4.4+ | Сборка проекта |
| Для соискателей | Element Plus | 2.3+ | UI компоненты |
| Для HR | Ant Design Vue | 3.2+ | UI компоненты |
| State management | Pinia | 2.1+ | Управление состоянием |
| HTTP клиент | Axios | 1.5+ | Запросы к API |
| Роутинг | Vue Router | 4.2+ | Навигация |
| Чарты | Chart.js | 4.3+ | Визуализация данных |
| Экспорт данных | xlsx | 0.18+ | Генерация Excel |

### Базы данных и хранилища
| Компонент | Технология | Версия | Назначение |
|-----------|------------|---------|------------|
| Основная БД | PostgreSQL | 15+ | Основное хранилище |
| Кэш | Redis | 7.2+ | Сессии, кэширование |
| Файловое хранилище | MinIO | Latest | Хранение файлов |
| Векторная БД | Qdrant | 1.7+ | Хранение эмбеддингов |
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
- **Базовый URL:** `https://api.career-ai.com`
- **Версионирование:** в URL пути (`/api/v1/*`)
- **Формат данных:** JSON для всех запросов и ответов
- **Аутентификация:** Bearer JWT токен
- **Коды ответов:** стандартные HTTP коды

### Разделение API:

#### API для соискателей: `https://api.career-ai.com/api/v1/seekers/*`
```yaml
# Аутентификация
POST /seekers/auth/register:
  summary: Регистрация соискателя
  description: Создание нового аккаунта соискателя
  
POST /seekers/auth/login:
  summary: Вход соискателя
  description: Аутентификация соискателя

# Резюме
POST /seekers/resumes/upload:
  summary: Загрузка резюме
  description: Загрузка и анализ резюме PDF/DOCX
  
GET /seekers/resumes/{id}/analysis:
  summary: Анализ резюме
  description: Подробный AI-анализ резюме с рекомендациями

# Вакансии
GET /seekers/vacancies/search:
  summary: Поиск вакансий
  description: Интеллектуальный поиск вакансий с фильтрами
  
POST /seekers/vacancies/{id}/apply:
  summary: Отклик на вакансию
  description: Автоматический отклик с адаптированным резюме

# AI помощник
POST /seekers/chat/message:
  summary: Отправить сообщение в AI-чат
  description: Взаимодействие с AI-помощником для подготовки
  
GET /seekers/interview/simulate:
  summary: Симуляция собеседования
  description: AI-симуляция собеседования для конкретной вакансии
```

#### API для HR: `https://api.career-ai.com/api/v1/hr/*`
```yaml
# Аутентификация компании
POST /hr/auth/register:
  summary: Регистрация компании
  description: Создание корпоративного аккаунта
  
POST /hr/auth/company/login:
  summary: Вход для компании
  description: Аутентификация HR-пользователя

# Управление вакансиями
POST /hr/vacancies:
  summary: Создание вакансии
  description: Публикация новой вакансии с AI-анализом требований
  
GET /hr/vacancies/{id}/candidates:
  summary: Получить кандидатов
  description: AI-ранжированный список кандидатов для вакансии

# Анализ кандидатов
POST /hr/candidates/bulk-upload:
  summary: Массовая загрузка резюме
  description: Загрузка и анализ множества резюме
  
GET /hr/candidates/{id}/evaluation:
  summary: Оценка кандидата
  description: Подробный AI-анализ кандидата с прогнозом успеха

# Аналитика
GET /hr/analytics/hiring-metrics:
  summary: Метрики подбора
  description: Аналитика процесса найма и эффективности
```

## 🗄️ Модели данных

### User (Базовый пользователь)
```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    user_type = Column(String(20), nullable=False)  # 'seeker', 'hr', 'company_admin'
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    subscription_tier = Column(String(50), default="free")
    subscription_ends_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    seeker_profile = relationship("SeekerProfile", back_populates="user", uselist=False)
    hr_profile = relationship("HrProfile", back_populates="user", uselist=False)
```

### SeekerProfile (Профиль соискателя)
```python
class SeekerProfile(Base):
    __tablename__ = "seeker_profiles"
    
    user_id = Column(UUID, ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(255))
    phone = Column(String(50))
    location = Column(String(255))
    current_position = Column(String(255))
    target_position = Column(String(255))
    experience_years = Column(Integer)
    expected_salary = Column(Integer)
    currency = Column(String(10), default="RUB")
    
    # Навыки и компетенции
    skills = Column(ARRAY(String))
    hard_skills = Column(JSONB)      # Технические навыки с уровнями
    soft_skills = Column(JSONB)      # Soft skills с оценками
    languages = Column(JSONB)        # Языки с уровнями
    
    # Предпочтения
    job_preferences = Column(JSONB)  # Тип занятости, формат работы и т.д.
    industry_preferences = Column(ARRAY(String))
    company_size_preference = Column(String(50))
    
    # Статус поиска
    search_status = Column(String(50), default="active")  # active, passive, not_looking
    search_started_at = Column(DateTime)
    
    # Relationships
    user = relationship("User", back_populates="seeker_profile")
    resumes = relationship("Resume", back_populates="seeker")
    applications = relationship("Application", back_populates="seeker")
```

### Company (Компания)
```python
class Company(Base):
    __tablename__ = "companies"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    legal_name = Column(String(255))
    industry = Column(String(100))
    description = Column(Text)
    website = Column(String(255))
    logo_url = Column(String(500))
    
    # Размер компании
    size = Column(String(50))  # startup, small, medium, large
    employee_count = Column(Integer)
    
    # Локация
    headquarters = Column(String(255))
    locations = Column(ARRAY(String))
    
    # Подписка
    subscription_tier = Column(String(50), default="starter")
    subscription_ends_at = Column(DateTime)
    features = Column(JSONB)  # Доступные функции
    
    # Контакты
    contact_email = Column(String(255))
    contact_phone = Column(String(50))
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    hr_users = relationship("HrProfile", back_populates="company")
    vacancies = relationship("Vacancy", back_populates="company")
```

### Resume (Резюме)
```python
class Resume(Base):
    __tablename__ = "resumes"
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    owner_type = Column(String(20), nullable=False)  # 'seeker', 'hr_uploaded'
    owner_id = Column(UUID, nullable=False)  # seeker_profile_id или company_id
    
    # Файл
    original_filename = Column(String(500))
    file_path = Column(String(500))
    file_size = Column(Integer)
    file_type = Column(String(50))
    
    # Парсированные данные
    parsed_data = Column(JSONB)
    raw_text = Column(Text)
    language = Column(String(10), default="ru")
    
    # Извлеченные поля
    full_name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    experience_years = Column(Integer)
    
    # Навыки (извлеченные AI)
    skills = Column(ARRAY(String))
    skill_categories = Column(JSONB)  # Группировка навыков по категориям
    skill_levels = Column(JSONB)      # Уровни навыков
    
    # Опыт работы
    work_experience = Column(JSONB)
    total_experience_months = Column(Integer)
    
    # Образование
    education = Column(JSONB)
    highest_degree = Column(String(100))
    
    # AI оценка
    ai_score = Column(Float)          # Общая оценка AI
    completeness_score = Column(Float) # Полнота резюме
    ats_score = Column(Float)         # Совместимость с ATS
    
    # Флаги
    is_primary = Column(Boolean, default=False)
    is_public = Column(Boolean, default=False)
    is_parsed = Column(Boolean, default=False)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    seeker = relationship("SeekerProfile", back_populates="resumes", 
                         foreign_keys=[owner_id], 
                         primaryjoin="and_(Resume.owner_type=='seeker', Resume.owner_id==SeekerProfile.user_id)")
    matches = relationship("MatchResult", back_populates="resume")
```

## 🔐 Безопасность

### Аутентификация
```python
# JWT конфигурация
JWT_CONFIG = {
    "algorithm": "HS256",
    "access_token_expire_minutes": 60 * 24,      # 24 часа
    "refresh_token_expire_days": 30,            # 30 дней
    "secret_key": os.getenv("JWT_SECRET_KEY"),
    
    # Разные аудитории для разных типов пользователей
    "audience": {
        "seekers": "career-ai-seekers",
        "hr": "career-ai-hr",
        "admin": "career-ai-admin"
    }
}
```

### Авторизация
```python
# Ролевая модель
ROLES = {
    "seeker": ["read_own_profile", "manage_own_resumes", "search_vacancies"],
    "hr_recruiter": ["read_company_profile", "manage_vacancies", "view_candidates"],
    "hr_manager": ["manage_team", "view_analytics", "manage_subscription"],
    "company_admin": ["manage_users", "manage_billing", "full_access"]
}

# Проверка владения ресурсом
def check_resource_ownership(user_id: UUID, resource_owner_id: UUID, resource_type: str):
    """Проверяет, имеет ли пользователь доступ к ресурсу"""
    if resource_type == "seeker":
        return user_id == resource_owner_id
    elif resource_type == "company":
        # Проверка через таблицу hr_profiles
        return is_user_in_company(user_id, resource_owner_id)
```

### Защита данных
```python
SECURITY_CONFIG = {
    # HTTPS обязателен
    "force_https": True,
    
    # Заголовки безопасности
    "security_headers": {
        "Content-Security-Policy": "default-src 'self'",
        "X-Frame-Options": "DENY",
        "X-Content-Type-Options": "nosniff",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Permissions-Policy": "geolocation=(), microphone=()"
    },
    
    # Шифрование
    "encryption": {
        "algorithm": "AES-256-GCM",
        "key_rotation_days": 90
    },
    
    # Rate limiting
    "rate_limits": {
        "anonymous": "100/hour",
        "seeker_free": "1000/hour",
        "seeker_pro": "5000/hour",
        "hr_starter": "10000/hour",
        "hr_business": "50000/hour"
    }
}
```

### Соответствие стандартам
- **GDPR:** для европейских пользователей
- **152-ФЗ:** для российских пользователей
- **ISO 27001:** базовые меры безопасности
- **OWASP Top 10:** защита от основных уязвимостей

## 🚀 Развертывание

### Требования к окружению
- **CPU:** минимум 4 ядра для продакшена
- **RAM:** минимум 8GB для продакшена
- **Storage:** минимум 50GB SSD
- **OS:** Ubuntu 22.04+ / Debian 11+ / Docker совместимые

### Docker конфигурация
```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  # Базы данных
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: career_ai
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Бэкенд сервисы
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.prod
    environment:
      DATABASE_URL: postgresql://${DB_USER}:${DB_PASSWORD}@postgres:5432/career_ai
      REDIS_URL: redis://:${REDIS_PASSWORD}@redis:6379
      JWT_SECRET_KEY: ${JWT_SECRET_KEY}
      HH_API_KEY: ${HH_API_KEY}
      OPENAI_API_KEY: ${OPENAI_API_KEY}
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    restart: unless-stopped
    ports:
      - "8000:8000"

  # Фронтенд сервисы
  frontend_seekers:
    build:
      context: ./frontend/seekers
      dockerfile: Dockerfile.prod
    environment:
      VITE_API_URL: https://api.career-ai.com
    restart: unless-stopped
    ports:
      - "3001:80"

  frontend_hr:
    build:
      context: ./frontend/hr
      dockerfile: Dockerfile.prod
    environment:
      VITE_API_URL: https://api.career-ai.com
    restart: unless-stopped
    ports:
      - "3002:80"

  # Nginx для проксирования
  nginx:
    image: nginx:alpine
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/ssl:/etc/nginx/ssl
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - backend
      - frontend_seekers
      - frontend_hr
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
  minio_data:
```

## 📊 Мониторинг и логирование

### Prometheus метрики
```yaml
# Конфигурация метрик
metrics:
  enabled: true
  path: /metrics
  port: 8000
  
  # Кастомные метрики
  custom_metrics:
    # Для соискателей
    - name: seekers_registered_total
      type: counter
      help: "Total number of seekers registered"
      labels: ["subscription_tier"]
    
    - name: resumes_analyzed_total
      type: counter
      help: "Total number of resumes analyzed"
      labels: ["user_type"]
    
    # Для HR
    - name: companies_registered_total
      type: counter
      help: "Total number of companies registered"
      labels: ["subscription_tier", "industry"]
    
    - name: vacancies_created_total
      type: counter
      help: "Total number of vacancies created"
      labels: ["company_size"]
    
    - name: candidates_evaluated_total
      type: counter
      help: "Total number of candidates evaluated"
      labels: ["evaluation_type"]
    
    # Системные
    - name: api_request_duration_seconds
      type: histogram
      help: "API request duration in seconds"
      labels: ["method", "endpoint", "status_code"]
    
    - name: ai_processing_duration_seconds
      type: histogram
      help: "AI processing duration in seconds"
      labels: ["model_type", "operation"]
```

### Логирование
```python
# Конфигурация логов
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": "%(asctime)s %(name)s %(levelname)s %(message)s %(user_id)s %(user_type)s %(request_id)s"
        },
        "console": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
            "level": "INFO"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/var/log/career-ai/app.log",
            "maxBytes": 10485760,  # 10MB
            "backupCount": 10,
            "formatter": "json",
            "level": "INFO"
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/var/log/career-ai/error.log",
            "maxBytes": 10485760,
            "backupCount": 10,
            "formatter": "json",
            "level": "ERROR"
        }
    },
    "loggers": {
        "": {  # Root logger
            "handlers": ["console", "file", "error_file"],
            "level": "INFO",
            "propagate": False
        },
        "uvicorn": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False
        },
        "sqlalchemy": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False
        }
    }
}
```

```

Вот переписанная README.md и техническая спецификация. Нужны остальные файлы?
