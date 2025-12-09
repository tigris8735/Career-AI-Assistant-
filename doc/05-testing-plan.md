# План тестирования: AI Career Scout

## 🎯 Общие сведения

**Проект:** AI Career Scout  
**Версия плана:** 2.0  
**Дата:** Q1 2024  
**Тип тестирования:** Полный цикл (E2E)  
**Ответственные:** QA Team, DevOps, Разработчики

## 📋 Область тестирования

### Включаемые модули:
1. **AI-тестирование навыков** — адаптивное тестирование на DeepSeek
2. **Парсинг HH.ru** — сбор и фильтрация вакансий
3. **Система рекомендаций** — матчинг резюме и вакансий
4. **Интеграции с министерствами** — массовая регистрация, отчеты
5. **Пользовательский интерфейс** — веб-приложение и PWA
6. **Производительность** — нагрузка на AI и парсинг
7. **Безопасность** — защита персональных данных

### Исключаемые модули:
1. Внутренняя логика DeepSeek API
2. Инфраструктура HH.ru
3. Системы министерств (только точки интеграции)

## 🧪 Типы тестирования

### 1. Модульное тестирование (Unit)
**Цель:** Проверка отдельных компонентов
**Покрытие:** ≥ 85% кода бэкенда
**Инструменты:** pytest, unittest, coverage.py
**Фокус:** Алгоритмы фильтрации, парсинг, логика тестирования

### 2. Интеграционное тестирование
**Цель:** Проверка взаимодействия с внешними API
**Сценарии:** 
- Интеграция с DeepSeek API 3.2
- Парсинг HH.ru (API + веб-скрапинг)
- Интеграция с API министерств
- Работа с очередями (Celery + RabbitMQ)

### 3. Системное тестирование (E2E)
**Цель:** Полные пользовательские сценарии
**Сценарии:**
- Регистрация → Тестирование → Поиск → Отклик
- Массовая регистрация студентов министерства
- Обработка большого объема вакансий
- Аварийное восстановление

### 4. Нагрузочное тестирование
**Цель:** Проверка под пиковой нагрузкой
**Инструменты:** locust, k6, JMeter
**Сценарии:** 
- Параллельное тестирование 1000+ пользователей
- Парсинг 100k+ вакансий в час
- AI-обработка 500+ резюме одновременно

### 5. Тестирование безопасности
**Цель:** Защита персональных данных
**Инструменты:** OWASP ZAP, Bandit, Snyk
**Фокус:** 
- Шифрование данных пользователей
- Защита API ключей
- Предотвращение инъекций
- Соответствие 152-ФЗ

### 6. UX тестирование
**Цель:** Удобство использования
**Методы:** 
- Юзабилити тестирование с реальными пользователями
- A/B тестирование интерфейсов
- Тестирование доступности (WCAG)

## 📋 Тестовые сценарии

### Модуль: Адаптивное тестирование

```gherkin
Feature: AI-тестирование навыков на основе резюме

  Scenario: Успешное прохождение технического тестирования
    Given Пользователь загрузил резюме разработчика
    When Он начинает адаптивное тестирование
    And Отвечает на вопросы разной сложности
    Then Система определяет уровень как "Middle"
    And Генерирует персональные рекомендации
    And Сохраняет результаты тестирования

  Scenario: Тестирование с некорректными ответами
    Given Пользователь проходит тестирование
    When Он дает заведомо неверные ответы
    Then Система адаптирует сложность вопросов
    And Понижает оценку уровня
    And Рекомендует повторить тестирование через неделю

  Scenario: Сбой интеграции с DeepSeek API
    Given DeepSeek API недоступен
    When Пользователь начинает тестирование
    Then Система переключается на локальные модели
    And Уведомляет пользователя о временных ограничениях
    And Логирует ошибку для анализа
```

### Модуль: Парсинг и фильтрация HH.ru

```gherkin
Feature: Сбор и фильтрация вакансий с HH.ru

  Scenario: Успешный парсинг качественных вакансий
    Given Система запускает ежедневный парсинг
    When Она обрабатывает 1000+ вакансий
    And Применяет AI-фильтры качества
    Then Отбирает 200+ качественных вакансий
    And Исключает 50+ проплаченных позиций
    And Обновляет базу данных

  Scenario: Обнаружение и обработка "затычек"
    Given Система анализирует вакансию
    When Обнаруживает признаки "затычки" (нулевая зарплата, шаблонный текст)
    Then Помечает вакансию как низкокачественную
    And Уменьшает ее приоритет в рекомендациях
    And Логирует для улучшения алгоритма

  Scenario: Обработка капчи и ограничений HH.ru
    Given HH.ru возвращает капчу
    When Система обнаруживает ограничение
    Then Временно приостанавливает парсинг
    And Использует альтернативные источники
    And Уведомляет администратора
```

### Модуль: Интеграция с министерствами

```gherkin
Feature: Массовая регистрация студентов

  Scenario: Импорт студентов федерального министерства
    Given Министерство предоставляет файл с 5000 студентов
    When Система обрабатывает импорт
    Then Создает 5000 аккаунтов
    And Назначает специальный тариф "Студент"
    And Отправляет приветственные письма
    And Формирует отчет об успешном импорте

  Scenario: Синхронизация данных с московским министерством
    Given API московского министерства доступно
    When Система выполняет синхронизацию
    Then Обновляет статусы студентов (активный/выпускник)
    And Обновляет информацию о программах обучения
    And Формирует отчет по трудоустройству
```

## ⚡ Нагрузочное тестирование

### Сценарии нагрузки:

```javascript
// k6 тест для API тестирования
import http from 'k6/http';
import { check, sleep } from 'k6';
import { SharedArray } from 'k6/data';

// Тестовые данные
const testData = new SharedArray('users', function() {
  return JSON.parse(open('./test-data/users.json'));
});

export const options = {
  stages: [
    { duration: '1m', target: 50 },    // Разогрев
    { duration: '3m', target: 200 },   // Средняя нагрузка
    { duration: '2m', target: 500 },   // Пиковая нагрузка
    { duration: '1m', target: 0 },     // Снижение
  ],
  thresholds: {
    http_req_duration: ['p(95)<3000'], // 95% запросов < 3 сек
    http_req_failed: ['rate<0.01'],    // < 1% ошибок
    'ai_processing_duration': ['p(95)<5000'], // AI обработка < 5 сек
  },
};

export default function() {
  const BASE_URL = 'https://api.career-scout.ru';
  const user = testData[__VU % testData.length];
  
  // 1. Регистрация
  const registerRes = http.post(`${BASE_URL}/api/v1/auth/register`, JSON.stringify({
    email: user.email,
    password: user.password,
    full_name: user.full_name,
    user_type: 'professional'
  }), {
    headers: { 'Content-Type': 'application/json' },
  });
  
  check(registerRes, {
    'register successful': (r) => r.status === 201,
  });
  
  const token = registerRes.json('access_token');
  
  // 2. Загрузка резюме
  const resumeRes = http.post(`${BASE_URL}/api/v1/resumes/upload`, {
    file: http.file(open('./test-data/resume.pdf'), 'resume.pdf'),
    title: 'Тестовое резюме'
  }, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  
  check(resumeRes, {
    'resume uploaded': (r) => r.status === 201,
  });
  
  const resumeId = resumeRes.json('id');
  
  // 3. Запуск тестирования
  const testRes = http.post(`${BASE_URL}/api/v1/testing/start`, JSON.stringify({
    test_type: 'technical',
    resume_id: resumeId
  }), {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
  });
  
  check(testRes, {
    'test started': (r) => r.status === 201,
  });
  
  sleep(2);
}
```

### Тестирование парсинга HH.ru:

```python
# locust тест для парсинга
from locust import HttpUser, task, between
import random

class HHParseUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def parse_vacancies(self):
        # Тестирование API парсинга
        response = self.client.post("/api/v1/vacancies/parse", json={
            "keywords": ["python", "developer"],
            "location": "Москва",
            "limit": 100
        })
        
        assert response.status_code == 202
        job_id = response.json().get("job_id")
        
        # Проверка статуса
        self.client.get(f"/api/v1/vacancies/parse/{job_id}/status")
    
    @task(1)
    def heavy_parse(self):
        # Тяжелый парсинг
        response = self.client.post("/api/v1/vacancies/parse", json={
            "keywords": ["разработчик"],
            "location": "Россия",
            "limit": 1000,
            "deep_parse": True
        })
        assert response.status_code == 202
    
    @task(5)
    def search_vacancies(self):
        # Поиск вакансий
        response = self.client.get("/api/v1/vacancies/search", params={
            "query": "python",
            "page": random.randint(1, 10),
            "per_page": 20
        })
        assert response.status_code == 200
        assert len(response.json().get("vacancies", [])) > 0
```

## 🔐 Тестирование безопасности

### Пентест сценарии:

```python
# Тестирование OWASP Top 10
class SecurityTests(unittest.TestCase):
    
    def test_sql_injection(self):
        """Тестирование на SQL инъекции"""
        # Попытка инъекции через параметры
        malicious_payload = "' OR '1'='1' --"
        
        response = requests.get(
            f"{BASE_URL}/api/v1/users",
            params={"email": malicious_payload},
            headers={"Authorization": f"Bearer {TEST_TOKEN}"}
        )
        
        # Должна вернуться ошибка валидации, не 500
        self.assertNotEqual(response.status_code, 500)
        self.assertNotIn("syntax error", response.text.lower())
    
    def test_xss_protection(self):
        """Тестирование защиты от XSS"""
        xss_payload = "<script>alert('xss')</script>"
        
        response = requests.post(
            f"{BASE_URL}/api/v1/resumes",
            json={"title": xss_payload, "content": "test"},
            headers={"Authorization": f"Bearer {TEST_TOKEN}"}
        )
        
        # Проверяем, что скрипты экранируются
        self.assertEqual(response.status_code, 400)
    
    def test_rate_limiting(self):
        """Тестирование ограничения запросов"""
        responses = []
        for i in range(101):  # Лимит 100 запросов в час
            response = requests.get(
                f"{BASE_URL}/api/v1/vacancies",
                headers={"Authorization": f"Bearer {TEST_TOKEN}"}
            )
            responses.append(response.status_code)
        
        # Последний запрос должен быть 429
        self.assertEqual(responses[-1], 429)
```

### Тестирование соответствия 152-ФЗ:

```python
class DataProtectionTests(unittest.TestCase):
    
    def test_personal_data_encryption(self):
        """Тестирование шифрования персональных данных"""
        # Проверяем, что чувствительные данные шифруются
        user_data = {
            "email": "test@example.com",
            "phone": "+79161234567",
            "passport": "4510 123456"
        }
        
        # Сохраняем в БД
        response = save_user_data(user_data)
        
        # Проверяем raw базу данных
        raw_data = get_raw_database_entry(response.user_id)
        
        # Email и телефон должны быть зашифрованы
        self.assertNotIn(user_data["email"], str(raw_data))
        self.assertNotIn(user_data["phone"], str(raw_data))
        # Паспортные данные вообще не должны сохраняться
        self.assertNotIn("passport", str(raw_data))
    
    def test_data_retention_policy(self):
        """Тестирование политики хранения данных"""
        # Создаем тестового пользователя
        user_id = create_test_user()
        
        # Удаляем пользователя
        delete_user(user_id)
        
        # Проверяем, что данные анонимизируются
        anonymized_data = get_user_data(user_id)
        self.assertEqual(anonymized_data["email"], "deleted@user.com")
        self.assertEqual(anonymized_data["phone"], None)
        
        # Проверяем срок хранения логов
        old_logs = get_logs_older_than(days=90)
        self.assertEqual(len(old_logs), 0)  # Логи старше 90 дней удаляются
```

## 📊 Критерии завершения тестирования

### Тестирование считается завершенным когда:

#### 1. Все критические и блокирующие дефекты исправлены:
- **Критические:** 0 дефектов
- **Высокий приоритет:** ≤ 2 дефектов
- **Средний приоритет:** ≤ 5 дефектов
- **Низкий приоритет:** ≤ 10 дефектов

#### 2. Достигнуто требуемое покрытие:
- **Бэкенд код:** ≥ 85% покрытия тестами
- **Фронтенд код:** ≥ 75% покрытия тестами
- **Критический функционал:** 100% покрытия

#### 3. Производительность соответствует требованиям:
- **API response time:** P95 < 2 секунды
- **AI processing time:** P95 < 5 секунд
- **Парсинг вакансий:** 1000+ вакансий/час
- **Обработка тестов:** 500+ одновременно

#### 4. Безопасность подтверждена:
- **OWASP Top 10:** Все уязвимости устранены
- **152-ФЗ:** Полное соответствие
- **Аудит безопасности:** Проведен независимой организацией
- **Penetration test:** Успешно пройден

#### 5. Пользовательское тестирование завершено:
- **Юзабилити тесты:** 50+ пользователей
- **A/B тесты:** Статистически значимые результаты
- **NPS:** ≥ 60 баллов
- **Удовлетворенность:** ≥ 4.5/5

#### 6. Документация обновлена:
- **Тест-кейсы:** 100% актуальны
- **Баг-репорты:** Все закрыты
- **Отчеты:** Сформированы и утверждены
- **Руководства:** Обновлены для пользователей

### Exit Criteria Matrix:

| Категория | Целевое значение | Фактическое значение | Статус |
|-----------|------------------|---------------------|--------|
| Критические дефекты | 0 | - | ⬜ |
| Покрытие бэкенд | ≥85% | - | ⬜ |
| Покрытие фронтенд | ≥75% | - | ⬜ |
| API latency (p95) | <2s | - | ⬜ |
| AI processing (p95) | <5s | - | ⬜ |
| Ошибки безопасности | 0 | - | ⬜ |
| NPS | ≥60 | - | ⬜ |
| Юзабилити score | ≥4.5/5 | - | ⬜ |

### Процесс приемки:

1. **Подготовительный этап:**
   - Все тесты выполнены
   - Отчеты сформированы
   - Дефекты классифицированы

2. **Review встреча:**
   - Презентация результатов команде
   - Обсуждение оставшихся дефектов
   - Принятие решения о готовности

3. **Подписание акта приемки:**
   - Product Owner подписывает акт
   - Фиксируются оставшиеся работы
   - Определяются сроки релиза

4. **Пострелизный мониторинг:**
   - Мониторинг метрик в production
   - Быстрое реагирование на инциденты
   - Сбор обратной связи от пользователей

## 📈 Метрики качества

### Ключевые метрики тестирования:

```yaml
testing_metrics:
  coverage:
    backend: 85%
    frontend: 75%
    critical_paths: 100%
  
  performance:
    api_response_p95: "2000ms"
    ai_processing_p95: "5000ms"
    vacancy_parsing_rate: "1000/hour"
    concurrent_users: 500
    
  reliability:
    defect_density: "< 0.5 defects/KLOC"
    mean_time_to_failure: "> 720 hours"
    availability: "99.9%"
    
  security:
    vulnerabilities_critical: 0
    vulnerabilities_high: 0
    compliance: "152-FZ, GDPR"
    
  user_experience:
    nps: "> 60"
    usability_score: "> 4.5/5"
    task_success_rate: "> 90%"
```

### Отслеживание прогресса:

```python
# Дашборд метрик тестирования
class TestingDashboard:
    def __init__(self):
        self.metrics = {
            'test_execution': {
                'total_tests': 0,
                'passed_tests': 0,
                'failed_tests': 0,
                'skipped_tests': 0,
                'success_rate': 0.0
            },
            'defect_tracking': {
                'critical': 0,
                'high': 0,
                'medium': 0,
                'low': 0,
                'total_open': 0
            },
            'coverage': {
                'backend': 0.0,
                'frontend': 0.0,
                'integration': 0.0
            },
            'performance': {
                'api_response_p95': 0,
                'ai_processing_p95': 0,
                'load_test_results': {}
            }
        }
    
    def update_metrics(self):
        """Обновление метрик из различных источников"""
        # Сбор данных из тестовых фреймворков
        self.metrics['test_execution'] = collect_test_results()
        
        # Сбор данных из системы управления дефектами
        self.metrics['defect_tracking'] = collect_defect_metrics()
        
        # Сбор данных coverage
        self.metrics['coverage'] = collect_coverage_data()
        
        # Сбор performance данных
        self.metrics['performance'] = collect_performance_metrics()
    
    def generate_report(self):
        """Генерация отчета о тестировании"""
        report = {
            'summary': self._generate_summary(),
            'detailed_metrics': self.metrics,
            'trends': self._calculate_trends(),
            'recommendations': self._generate_recommendations()
        }
        return report
```

## 🚀 Заключение

План тестирования AI Career Scout охватывает все аспекты качества системы, от юнит-тестов до полноценного E2E тестирования с реальными пользователями. Особое внимание уделяется:

1. **Надежности AI-компонентов** — тестирование интеграции с DeepSeek
2. **Производительности парсинга** — обработка больших объемов данных
3. **Безопасности персональных данных** — соответствие 152-ФЗ
4. **Удобству использования** — юзабилити тестирование с целевой аудиторией

Система тестирования построена по принципу непрерывной интеграции, где каждый коммит проходит через полный цикл проверок, что позволяет выявлять проблемы на ранних этапах и обеспечивать высокое качество продукта.

---

*Последнее обновление: 20 января 2024*  
*Версия плана тестирования: 2.0*  
*© 2024 AI Career Scout QA Team
