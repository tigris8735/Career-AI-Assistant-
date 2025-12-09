# Техническая спецификация: AI Career Scout

## 📋 Общие сведения

**Название проекта:** AI Career Scout  
**Версия спецификации:** 2.0  
**Дата:** Q4 2024  
**Целевые платформы:** Web, PWA, Telegram, API  
**Архитектура:** Микросервисная на базе событий

## 🛠️ Технологический стек

### AI & ML слой
| Компонент | Технология | Версия | Назначение |
|-----------|------------|---------|------------|
| Основной AI движок | DeepSeek API | 3.2 | Генерация тестов, оценка |
| Fine-tuning | DeepSeek Fine-tuning API | Latest | Кастомизация под вакансии |
| NLP обработка | spaCy + NLTK | 3.7+ | Анализ резюме и вакансий |
| Классификация | scikit-learn | 1.3+ | Фильтрация вакансий |
| Векторные эмбеддинги | sentence-transformers | 2.2+ | Семантический поиск |

### Backend сервисы
| Сервис | Технология | Назначение |
|--------|------------|------------|
| API Gateway | FastAPI + Kong | Единая точка входа |
| Auth Service | FastAPI + JWT | Аутентификация |
| Testing Service | FastAPI + WebSocket | Адаптивное тестирование |
| Vacancy Service | FastAPI + Celery | Парсинг и обработка |
| Matching Service | FastAPI + Redis | Рекомендации |
| Ministry Service | FastAPI | Интеграции с гос.системами |

### Базы данных и хранилища
| Тип | Технология | Конфигурация | Назначение |
|-----|------------|--------------|------------|
| Основная БД | PostgreSQL 16 | 3 ноды, репликация | Пользователи, вакансии |
| Кэш | Redis 7.2 | Кластер 6 нод | Сессии, результаты |
| Поиск | Elasticsearch 8.11 | 3 ноды | Поиск по вакансиям |
| Файлы | MinIO | S3-совместимое | Резюме, логи |
| Очереди | RabbitMQ 4.0 | Кластер | Асинхронные задачи |

### Frontend
| Платформа | Технология | Особенности |
|-----------|------------|-------------|
| Web | Vue 3 + TypeScript | SPA с SSR |
| Мобильное | PWA (Vue + Capacitor) | Оффлайн режим |
| Telegram | Node.js + Telegraf | Уведомления, быстрый доступ |
| Админка | Vue 3 + Naive UI | Управление системой |

### DevOps & Инфраструктура
| Категория | Технологии |
|-----------|------------|
| Контейнеризация | Docker 24.0+, Kubernetes 1.28 |
| CI/CD | GitLab CI/CD, ArgoCD |
| Мониторинг | Prometheus, Grafana, Loki, Tempo |
| Логирование | ELK Stack (Elastic, Logstash, Kibana) |
| Хостинг | Yandex Cloud Managed Kubernetes |
| CDN | Cloudflare + Yandex CDN |

## 📊 API Спецификация

### Базовые параметры:
- **Базовый URL:** `https://api.career-scout.ru/api/v1`
- **Формат:** JSON для запросов/ответов
- **Аутентификация:** Bearer JWT + API Keys для министерств
- **Rate limiting:** Зависит от подписки (100-10000 запросов/час)

### Ключевые эндпоинты:

#### Адаптивное тестирование
```yaml
POST /testing/start:
  summary: Начать адаптивное тестирование
  security:
    - bearerAuth: []
  requestBody:
    required: true
    content:
      application/json:
        schema:
          type: object
          properties:
            test_type:
              type: string
              enum: [technical, soft_skills, combined]
            resume_id:
              type: string
              format: uuid
  responses:
    201:
      description: Сессия тестирования создана
      content:
        application/json:
          schema:
            type: object
            properties:
              session_id:
                type: string
                format: uuid
              websocket_url:
                type: string
    400:
      description: Неверные параметры теста

GET /testing/{session_id}/next:
  summary: Получить следующий вопрос
  parameters:
    - name: session_id
      in: path
      required: true
      schema:
        type: string
        format: uuid
  responses:
    200:
      description: Вопрос для тестирования
      content:
        application/json:
          schema:
            type: object
            properties:
              question_id:
                type: string
              question_type:
                type: string
              question_text:
                type: string
              options:
                type: array
                items:
                  type: string
              time_limit:
                type: integer
    404:
      description: Сессия не найдена
```

#### Умный поиск вакансий
```yaml
POST /vacancies/search:
  summary: Поиск персональных вакансий
  security:
    - bearerAuth: []
  requestBody:
    required: true
    content:
      application/json:
        schema:
          type: object
          properties:
            test_session_id:
              type: string
              format: uuid
            filters:
              type: object
              properties:
                locations:
                  type: array
                  items:
                    type: string
                salary_min:
                  type: integer
                remote_only:
                  type: boolean
                experience_level:
                  type: string
                  enum: [junior, middle, senior]
  responses:
    200:
      description: Найденные вакансии
      content:
        application/json:
          schema:
            type: object
            properties:
              vacancies:
                type: array
                items:
                  $ref: '#/components/schemas/Vacancy'
              search_metadata:
                type: object
                properties:
                  total_found:
                    type: integer
                  quality_score:
                    type: number
                  search_time:
                    type: number
```

#### Интеграция с министерствами
```yaml
POST /ministry/federal/bulk:
  summary: Массовая регистрация студентов
  security:
    - apiKeyAuth: []
  requestBody:
    required: true
    content:
      application/json:
        schema:
          type: object
          properties:
            institute_id:
              type: string
            students:
              type: array
              items:
                type: object
                properties:
                  email:
                    type: string
                  full_name:
                    type: string
                  student_id:
                    type: string
                  program:
                    type: string
  responses:
    202:
      description: Регистрация принята в обработку
      content:
        application/json:
          schema:
            type: object
            properties:
              job_id:
                type: string
              estimated_time:
                type: integer
```

## 🔐 Безопасность и соответствие

### Модель безопасности:
```
Уровень 1: Пользовательский (JWT токены)
Уровень 2: Сервисный (API Keys между микросервисами)
Уровень 3: Министерский (mTLS + специфичные ключи)
Уровень 4: Административный (OAuth 2.0 + 2FA)
```

### Соответствие требованиям:
1. **152-ФЗ РФ** - обработка персональных данных
2. **GDPR** - для международных пользователей
3. **API HH.ru** - соблюдение лимитов и правил
4. **Гос.стандарты** - для интеграции с министерствами

### Шифрование данных:
```yaml
В движении:
  - TLS 1.3 для всех соединений
  - Сертификаты от Let's Encrypt + Yandex Cloud

В покое:
  - AES-256 для персональных данных
  - База данных: прозрачное шифрование
  - Файлы: шифрование на стороне клиента
```

## 📈 Масштабируемость

### Горизонтальное масштабирование:
```yaml
Микросервисы:
  testing-service: 3-10 реплик (в зависимости от нагрузки)
  vacancy-service: 5-15 реплик (парсинг тяжелый)
  matching-service: 3-8 реплик
  api-gateway: 2-5 реплик

Базы данных:
  PostgreSQL: Master + 2 Replicas (чтение)
  Redis: Cluster 6 нод (3 master, 3 replica)
  Elasticsearch: 3 ноды (поиск)
```

### Auto-scaling правила:
```yaml
По CPU:
  - Средняя загрузка > 70% → +1 реплика
  - Средняя загрузка < 30% → -1 реплика

По памяти:
  - Использование > 80% → +1 реплика

По времени:
  - Пиковые часы (10:00-12:00, 14:00-16:00) → дополнительные реплики
```

## 🧪 Тестирование и качество

### Типы тестов:
```python
# Unit тесты - покрытие > 90%
pytest tests/unit/

# Интеграционные тесты
pytest tests/integration/

# E2E тесты (Playwright)
npm run test:e2e

# Нагрузочное тестирование (Locust)
locust -f tests/load/locustfile.py

# Безопасность (OWASP ZAP)
zap-baseline.py -t https://api.career-scout.ru
```

### Метрики качества:
- **Availability:** 99.95% SLA
- **P95 Latency:** < 2 секунды
- **Error rate:** < 0.1%
- **Test coverage:** > 85%
- **MTTR:** < 15 минут

## 🚀 Деплой и CI/CD

### Pipeline этапы:
```yaml
stages:
  - lint         # Проверка кода
  - test         # Unit тесты
  - build        # Сборка Docker образов
  - security     # Сканирование безопасности
  - deploy-dev   # Деплой на dev
  - integration  # Интеграционные тесты
  - deploy-staging # Деплой на staging
  - e2e          # E2E тесты
  - deploy-prod  # Деплой на production
```

### Стратегия деплоя:
```yaml
production:
  strategy: blue-green
  health_checks:
    - path: /health
      timeout: 5s
      interval: 10s
    - path: /api/v1/health
      timeout: 5s
      interval: 10s
  
rollback:
  automatic: true
  conditions:
    - error_rate > 5%
    - p95_latency > 5s
    - failed_health_checks > 3
```
