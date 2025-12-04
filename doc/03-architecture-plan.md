# План архитектуры системы

## 🏗️ Общая архитектурная схема

```
┌─────────────────────────────────────────────────────────────┐
│                    Двусторонняя платформа                   │
├─────────────────────────────────────────────────────────────┤
│   Для соискателей              │    Для HR/компаний         │
│   • Анализ резюме              │    • Анализ кандидатов     │
│   • Поиск вакансий             │    • Управление вакансиями │
│   • AI-подготовка              │    • Автоматизация отбора  │
│   • Автоотклики                │    • Аналитика подбора     │
└──────────────┬─────────────────┴──────────────┬─────────────┘
               │                                │
               ▼                                ▼
┌─────────────────────────────────────────────────────────────┐
│                  Общий бэкенд слой                           │
│           (Микросервисы с разделением доступа)              │
└──────────────┬─────────────────┬──────────────┬─────────────┘
               │                 │              │
               ▼                 ▼              ▼
┌──────────────┴─────┐  ┌───────┴──────┐  ┌─────┴──────────┐
│   Auth Service     │  │  AI Engine   │  │ Matching      │
│   (Role-based)     │  │  (ML/AI)     │  │  Service       │
└──────────┬─────────┘  └───────┬──────┘  └──────┬─────────┘
           │                    │                 │
           └────────────────────┼─────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                   Интеграции и данные                        │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ HH.ru API│LinkedIn  │Платежи   │Email/SMS │   Хранилище     │
│          │API       │Gateway   │Services  │   данных        │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘
```

## 📁 Структура проекта

### Корневая структура
```
career_ai_assistant/
│
├── backend/                    # Основной бэкенд
│   ├── app/
│   │   ├── api/
│   │   │   ├── seekers/       # API для соискателей
│   │   │   │   ├── auth.py
│   │   │   │   ├── resumes.py
│   │   │   │   ├── vacancies.py
│   │   │   │   ├── chat.py
│   │   │   │   └── analytics.py
│   │   │   ├── hr/           # API для HR
│   │   │   │   ├── auth.py
│   │   │   │   ├── candidates.py
│   │   │   │   ├── vacancies.py
│   │   │   │   └── analytics.py
│   │   │   └── common/       # Общие API
│   │   │       ├── files.py
│   │   │       └── integrations.py
│   │   ├── models/
│   │   │   ├── seekers.py    # Модели для соискателей
│   │   │   ├── hr.py         # Модели для HR
│   │   │   └── common.py     # Общие модели
│   │   └── services/
│   │       ├── ai/
│   │       │   ├── resume_analyzer.py      # Анализ резюме
│   │       │   ├── vacancy_matcher.py      # Сопоставление
│   │       │   ├── interview_trainer.py    # Подготовка к собеседованиям
│   │       │   └── candidate_evaluator.py  # Оценка кандидатов
│   │       └── integrations/
│   │           ├── hh_api.py          # HH.ru интеграция
│   │           ├── linkedin_api.py    # LinkedIn интеграция
│   │           └── payment_gateways.py # Платежные системы
│
├── frontend/                  # Фронтенд приложения
│   ├── seekers/              # Приложение для соискателей
│   │   ├── src/
│   │   │   ├── views/
│   │   │   │   ├── Dashboard.vue      # Личный кабинет
│   │   │   │   ├── ResumeAnalysis.vue # Анализ резюме
│   │   │   │   ├── JobSearch.vue      # Поиск вакансий
│   │   │   │   ├── InterviewPrep.vue  # Подготовка
│   │   │   │   └── Settings.vue       # Настройки
│   │   │   └── components/
│   │   │       ├── ResumeUploader.vue
│   │   │       ├── JobCard.vue
│   │   │       ├── MatchScore.vue
│   │   │       └── ChatAssistant.vue
│   │   └── package.json
│   │
│   ├── hr/                   # Приложение для HR
│   │   ├── src/
│   │   │   ├── views/
│   │   │   │   ├── Dashboard.vue      # Аналитика
│   │   │   │   ├── Candidates.vue     # Кандидаты
│   │   │   │   ├── Vacancies.vue      # Вакансии
│   │   │   │   ├── Reports.vue        # Отчеты
│   │   │   │   └── CompanySettings.vue
│   │   │   └── components/
│   │   │       ├── CandidateTable.vue
│   │   │       ├── VacancyForm.vue
│   │   │       ├── ResumeAnalyzer.vue
│   │   │       └── AnalyticsDashboard.vue
│   │   └── package.json
│   │
│   └── landing/              # Лендинг и общая информация
│       ├── src/
│       │   ├── pages/
│       │   │   ├── Home.vue           # Главная
│       │   │   ├── ForSeekers.vue     # Для соискателей
│       │   │   ├── ForCompanies.vue   # Для компаний
│       │   │   ├── Pricing.vue        # Цены
│       │   │   └── Blog.vue           # Блог
│       │   └── components/
│       │       ├── HeroSection.vue
│       │       ├── FeatureCards.vue
│       │       └── Testimonials.vue
│       └── package.json
│
├── ml_pipeline/              # ML модели и AI
│   ├── models/
│   │   ├── resume_parser/    # Парсинг резюме
│   │   ├── skill_matcher/    # Сопоставление навыков
│   │   ├── interview_sim/    # Симулятор собеседований
│   │   └── success_predictor/# Прогноз успеха
│   ├── training/
│   │   ├── datasets/         # Датасеты
│   │   ├── scripts/          # Скрипты обучения
│   │   └── evaluation/       # Оценка моделей
│   └── deployment/           # Деплой моделей
│
├── docs/                     # Документация
│   ├── api/
│   │   ├── seekers_api.md    # API для соискателей
│   │   ├── hr_api.md         # API для HR
│   │   └── integration_api.md
│   ├── user-guides/
│   │   ├── seekers_guide.md  # Руководство для соискателей
│   │   ├── hr_guide.md       # Руководство для HR
│   │   └── admin_guide.md    # Администраторам
│   └── development/
│       ├── architecture.md
│       ├── deployment.md
│       └── contributing.md
│
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🔧 Компоненты системы

### 1. Backend Services

#### API Gateway:
- **Роутинг запросов** в зависимости от типа пользователя
- **Аутентификация и авторизация** с ролевой моделью
- **Rate limiting** по тарифам

#### Для соискателей:
```python
POST   /api/v1/seekers/auth/register       # Регистрация
POST   /api/v1/seekers/resumes/upload      # Загрузка резюме
GET    /api/v1/seekers/vacancies/search    # Поиск вакансий
POST   /api/v1/seekers/vacancies/{id}/apply # Отклик
GET    /api/v1/seekers/analytics/progress  # Прогресс
POST   /api/v1/seekers/chat/message        # AI-чат
```

#### Для HR:
```python
POST   /api/v1/hr/auth/register            # Регистрация компании
POST   /api/v1/hr/vacancies                # Создание вакансии
GET    /api/v1/hr/candidates               # Поиск кандидатов
POST   /api/v1/hr/candidates/{id}/evaluate # Оценка кандидата
GET    /api/v1/hr/analytics/hiring         # Аналитика найма
POST   /api/v1/hr/candidates/bulk-upload   # Массовая загрузка
```

### 2. AI Engine Components

#### Resume Analyzer:
```python
class ResumeAnalyzer:
    def parse_resume(file):           # Парсинг резюме
    def extract_skills(text):         # Извлечение навыков
    def evaluate_quality(resume):     # Оценка качества
    def suggest_improvements(resume): # Рекомендации по улучшению
    
    # Для HR:
    def batch_analyze(resumes):       # Массовый анализ
    def find_red_flags(resume):       # Поиск проблем
    def rank_candidates(resumes, vacancy): # Ранжирование
```

#### Interview Simulator:
```python
class InterviewSimulator:
    def generate_questions(vacancy):  # Генерация вопросов
    def evaluate_answer(answer):      # Оценка ответов
    def provide_feedback():           # Обратная связь
    def simulate_interview():         # Полная симуляция
```

### 3. Database Schema

```sql
-- Пользователи
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    user_type VARCHAR(20) CHECK (user_type IN ('seeker', 'hr', 'admin')),
    subscription_tier VARCHAR(50),
    created_at TIMESTAMP
);

-- Соискатели
CREATE TABLE seekers (
    user_id UUID REFERENCES users(id),
    full_name VARCHAR(255),
    current_position VARCHAR(255),
    experience_years INTEGER,
    skills TEXT[],
    job_preferences JSONB,
    search_status VARCHAR(50)
);

-- Компании и HR
CREATE TABLE companies (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    industry VARCHAR(100),
    size VARCHAR(50),
    subscription_tier VARCHAR(50)
);

CREATE TABLE hr_users (
    user_id UUID REFERENCES users(id),
    company_id UUID REFERENCES companies(id),
    role VARCHAR(50),
    permissions JSONB
);

-- Резюме
CREATE TABLE resumes (
    id UUID PRIMARY KEY,
    owner_type VARCHAR(20),
    owner_id UUID,
    original_file VARCHAR(500),
    parsed_data JSONB,
    skills TEXT[],
    is_public BOOLEAN DEFAULT false,
    created_at TIMESTAMP
);

-- Вакансии
CREATE TABLE vacancies (
    id UUID PRIMARY KEY,
    company_id UUID REFERENCES companies(id),
    title VARCHAR(500),
    requirements JSONB,
    status VARCHAR(50),
    source VARCHAR(50)
);

-- Сопоставления
CREATE TABLE matches (
    id UUID PRIMARY KEY,
    vacancy_id UUID REFERENCES vacancies(id),
    resume_id UUID REFERENCES resumes(id),
    match_score DECIMAL(5,2),
    status VARCHAR(50),
    predicted_success DECIMAL(3,2),
    created_at TIMESTAMP
);
```

## 🌐 Сетевая архитектура

```
Пользователи → Cloudflare CDN → Load Balancer → 
→ [Frontend: Seekers App]    [Frontend: HR App]    [Landing]
          ↓                        ↓                   ↓
    ┌─────────────────────────────────────────────┐
    │              API Gateway (Kong)             │
    └──────────────┬──────────────┬──────────────┘
                   │              │
           [Seekers API]    [HR API]
                   │              │
    ┌──────────────┴──────────────┴──────────────┐
    │            Микросервисы                     │
    ├──────────┬──────────┬──────────┬───────────┤
    │   Auth   │   AI     │ Matching │ Integra-  │
    │ Service  │ Engine   │ Service  │ tions     │
    └──────────┴──────────┴──────────┴───────────┘
                   │              │
    ┌──────────────┴──────────────┴──────────────┐
    │              Базы данных                    │
    ├──────────┬──────────┬──────────┬───────────┤
    │PostgreSQL│  Redis   │  MinIO   │ RabbitMQ  │
    │ Primary  │ (Кэш)    │(Файлы)   │(Очереди)  │
    └──────────┴──────────┴──────────┴───────────┘
```

## 🔄 Потоки данных

### Поток для соискателя:
```
1. Регистрация → Создание профиля → Загрузка резюме
2. AI анализирует резюме → Предлагает улучшения
3. Поиск вакансий → AI ранжирует по релевантности
4. Адаптация резюме под вакансию → Автоотклик
5. Подготовка к собеседованию → AI симуляция
6. Отслеживание прогресса → Аналитика
```

### Поток для HR:
```
1. Регистрация компании → Настройка профиля
2. Создание вакансии → AI анализ требований
3. Поиск кандидатов → AI фильтрация и ранжирование
4. Массовый анализ резюме → Выявление лучших
5. Оценка кандидатов → Прогноз успешности
6. Аналитика процесса → Оптимизация найма
```

## 🚀 Стратегия развертывания

### Фаза 1: MVP (0-3 месяца)
- Фокус на соискателей
- Базовый функционал анализа резюме
- Интеграция только с HH.ru
- Простая подписка

### Фаза 2: Расширение (3-6 месяцев)
- Добавление HR модуля
- Расширение AI возможностей
- Интеграция с LinkedIn
- Раздельные тарифы

### Фаза 3: Масштабирование (6-12 месяцев)
- Enterprise решения
- White-label для рекрутинговых агентств
- Расширение на СНГ
- Мобильные приложения

## 📈 Мониторинг и аналитика

### Метрики для мониторинга:
1. **Для соискателей:**
   - Конверсия регистраций в активных пользователей
   - Среднее время анализа резюме
   - Успешность откликов
   - Удовлетворенность AI-чат

2. **Для HR:**
   - Количество обработанных резюме
   - Время на подбор одного кандидата
   - Качество AI рекомендаций
   - Retention корпоративных клиентов

3. **Системные:**
   - Uptime > 99.5%
   - API response time p95 < 2s
   - Ошибки обработки файлов < 1%

### Логирование:
- Раздельные логи для seeker и HR операций
- Детальное логирование AI-решений
- Аудиторские логи для корпоративных клиентов
- Интеграция с Sentry для ошибок

Теперь продукт четко позиционируется как **двусторонняя платформа** с отдельными функциональностями для:
1. **Соискателей** - поиск работы, улучшение резюме, подготовка
2. **HR/компаний** - подбор кандидатов, автоматизация рекрутинга, аналитика

Каждый модуль имеет свою ценность и отдельный пользовательский опыт, но использует общий AI-движок и инфраструктуру.
