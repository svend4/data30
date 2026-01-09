# data30 API Documentation (Markdown)

## Format
This document is written in **Markdown**.

## API Versioning
* **Current version:** `v1`
* **Base URL:** `https://api.example.com/v1`
* **Versioning strategy:** URL prefix (`/v1/...`).

## Authentication
* **Scheme:** Bearer token (JWT or opaque token).
* **Header:** `Authorization: Bearer <token>`
* **Unauthenticated endpoints:** `GET /health`.

## Endpoints

### Health Check
**GET** `/health`  
Returns service status.

**Response (200)**
```json
{
  "status": "ok",
  "timestamp": "2025-01-01T12:00:00Z"
}
```

### List Items
**GET** `/items`  
Returns a paginated list of items.

**Query Parameters**
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `page` | integer | no | Page number (default: 1). |
| `page_size` | integer | no | Items per page (default: 20, max: 100). |

**Response (200)**
```json
{
  "data": [
    {
      "id": "item_123",
      "name": "Example Item",
      "created_at": "2025-01-01T12:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total": 1
  }
}
```

### Create Item
**POST** `/items`  
Creates a new item. **Requires authentication.**

**Request Body**
```json
{
  "name": "New Item"
}
```

**Response (201)**
```json
{
  "id": "item_124",
  "name": "New Item",
  "created_at": "2025-01-01T12:30:00Z"
}
```

### Get Item
**GET** `/items/{item_id}`  
Returns a single item by ID.

**Path Parameters**
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `item_id` | string | yes | Unique item identifier. |

**Response (200)**
```json
{
  "id": "item_123",
  "name": "Example Item",
  "created_at": "2025-01-01T12:00:00Z"
}
```

### Update Item
**PATCH** `/items/{item_id}`  
Updates an item. **Requires authentication.**

**Request Body**
```json
{
  "name": "Updated Item"
}
```

**Response (200)**
```json
{
  "id": "item_123",
  "name": "Updated Item",
  "updated_at": "2025-01-01T13:00:00Z"
}
```

### Delete Item
**DELETE** `/items/{item_id}`  
Deletes an item. **Requires authentication.**

**Response (204)**
No content.

## Schemas

### Item
```json
{
  "id": "string",
  "name": "string",
  "created_at": "RFC3339 timestamp",
  "updated_at": "RFC3339 timestamp (optional)"
}
```

### Error
```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": "object (optional)"
  }
}
```

## Errors and Status Codes
| Status | Meaning | Example Scenario |
| --- | --- | --- |
| 200 | OK | Successful read. |
| 201 | Created | Successful create. |
| 204 | No Content | Successful delete. |
| 400 | Bad Request | Invalid query or payload. |
| 401 | Unauthorized | Missing/invalid token. |
| 403 | Forbidden | Insufficient permissions. |
| 404 | Not Found | Item does not exist. |
| 409 | Conflict | Duplicate resource. |
| 429 | Too Many Requests | Rate limit exceeded. |
| 500 | Internal Server Error | Unexpected server error. |

**Error Response Example (400)**
```json
{
  "error": {
    "code": "INVALID_PAYLOAD",
    "message": "The field 'name' is required."
  }
}
```
# data30

## API scope
This document defines CRUD operations, endpoints, data contracts, and API requirements for:

- Function
- Module
- UseCase
- Macro

## 1. CRUD operations
All resources support the following base operations:

- Create: add a new entity.
- Read: fetch a single entity by id.
- Update: replace or partially update an entity by id.
- Delete: remove an entity by id (soft-delete by default).

## 2. Endpoints (REST)
Base path: `/api/v1`

### Functions
- `POST /functions`
- `GET /functions`
- `GET /functions/{functionId}`
- `PUT /functions/{functionId}`
- `PATCH /functions/{functionId}`
- `DELETE /functions/{functionId}`

### Modules
- `POST /modules`
- `GET /modules`
- `GET /modules/{moduleId}`
- `PUT /modules/{moduleId}`
- `PATCH /modules/{moduleId}`
- `DELETE /modules/{moduleId}`

### Use Cases
- `POST /use-cases`
- `GET /use-cases`
- `GET /use-cases/{useCaseId}`
- `PUT /use-cases/{useCaseId}`
- `PATCH /use-cases/{useCaseId}`
- `DELETE /use-cases/{useCaseId}`

### Macros
- `POST /macros`
- `GET /macros`
- `GET /macros/{macroId}`
- `PUT /macros/{macroId}`
- `PATCH /macros/{macroId}`
- `DELETE /macros/{macroId}`

## 3. Data contracts (OpenAPI-like JSON schemas)
All entities share these common fields:

```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

### Function
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "moduleId": "uuid",
  "signature": "string",
  "returnType": "string",
  "parameters": [
    {
      "name": "string",
      "type": "string",
      "required": true
    }
  ],
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

### Module
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "owner": "string",
  "version": "string",
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

### UseCase
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "moduleIds": ["uuid"],
  "functionIds": ["uuid"],
  "steps": [
    {
      "order": 1,
      "summary": "string",
      "macroId": "uuid|null"
    }
  ],
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

### Macro
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string|null",
  "inputs": [
    {
      "name": "string",
      "type": "string",
      "required": true
    }
  ],
  "outputs": [
    {
      "name": "string",
      "type": "string"
    }
  ],
  "steps": [
    {
      "order": 1,
      "action": "string",
      "functionId": "uuid|null"
    }
  ],
  "tags": ["string"],
  "createdAt": "date-time",
  "updatedAt": "date-time",
  "deletedAt": "date-time|null"
}
```

#### Request/response conventions
- Create request: omit `id`, `createdAt`, `updatedAt`, `deletedAt`.
- Update request (PUT): full resource without immutable fields (`id`, `createdAt`).
- Update request (PATCH): only fields to modify.
- Responses return the full resource.
- Errors use a standard envelope:

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": {}
  }
}
```

## 4. Filtering, pagination, sorting, versioning

### Filtering
Common query parameters for list endpoints:
- `ids`: comma-separated list of ids.
- `name`: substring match.
- `tags`: comma-separated list; matches any tag.
- `createdFrom`, `createdTo`: date-time range.
- `updatedFrom`, `updatedTo`: date-time range.
- `deleted`: boolean; include soft-deleted records if `true`.

Resource-specific filters:
- Functions: `moduleId`, `returnType`, `parameterType`.
- Modules: `owner`, `version`.
- UseCases: `moduleId`, `functionId`, `macroId`.
- Macros: `inputType`, `outputType`.

### Pagination
- `limit`: integer, default 25, max 100.
- `cursor`: opaque cursor for forward pagination.
- Response includes:
  - `items`: array of resources
  - `nextCursor`: string|null
  - `total`: integer (optional for performance-sensitive endpoints)

### Sorting
- `sort`: field name, prefix with `-` for descending.
  - Example: `sort=-updatedAt`
- Allowed fields: `name`, `createdAt`, `updatedAt`.

### API versioning
- URI versioning: `/api/v1`.
- Backward-incompatible changes require a new major version.
- Deprecations are announced with `Deprecation` and `Sunset` headers.
## 1. Список вертикалей

1. Маркетинг
2. Продажи
3. HR
4. Документооборот
5. Поддержка клиентов
6. Финансы

## 2–4. Сценарии, pipeline, шаги и сопоставление функций/приложений

### Вертикаль: Маркетинг

| Сценарий | Pipeline (шаги → входы → выходы → роли) | Функции и приложения по шагам |
| --- | --- | --- |
| Запуск рекламной кампании | 1) Бриф (вход: бизнес-цели, аудитория; выход: медиабриф; роли: маркетолог, бренд-менеджер) → 2) Планирование (вход: медиабриф; выход: медиаплан; роли: маркетолог, аналитик) → 3) Настройка (вход: медиаплан, креативы; выход: активные кампании; роли: performance-специалист) → 4) Оптимизация (вход: метрики; выход: обновленные ставки/таргетинг; роли: performance-специалист) → 5) Отчет (вход: данные; выход: отчет; роли: аналитик) | 1) Управление брифами (Confluence/Notion) 2) Планирование бюджета (Google Sheets/BI) 3) Запуск кампаний (Google Ads/Meta Ads) 4) Оптимизация ставок (Google Ads/Meta Ads) 5) Отчетность (Looker/Power BI) |
| Контент-маркетинг | 1) План (вход: цели, темы; выход: контент-план; роли: контент-менеджер) → 2) Производство (вход: ТЗ; выход: материалы; роли: редактор, дизайнер) → 3) Публикация (вход: материалы; выход: посты/страницы; роли: контент-менеджер) → 4) Дистрибуция (вход: посты; выход: охваты; роли: SMM) → 5) Аналитика (вход: метрики; выход: инсайты; роли: аналитик) | 1) Контент-план (Airtable/Notion) 2) Создание контента (Figma/Google Docs) 3) CMS публикация (WordPress/Tilda) 4) SMM (Hootsuite/Buffer) 5) Аналитика (GA4/Looker) |
| Email-рассылки | 1) Сегментация (вход: база; выход: сегменты; роли: CRM-менеджер) → 2) Создание писем (вход: ТЗ; выход: шаблоны; роли: копирайтер, дизайнер) → 3) Настройка отправки (вход: шаблоны; выход: кампании; роли: CRM-менеджер) → 4) Отправка (вход: кампании; выход: доставки; роли: CRM-менеджер) → 5) Анализ (вход: метрики; выход: отчет; роли: аналитик) | 1) Сегментация (CDP/CRM) 2) Шаблоны (Figma/Email Builder) 3) Кампании (Mailchimp/UniSender) 4) Отправка (ESP) 5) Аналитика (ESP/BI) |
| Вебинары | 1) Планирование (вход: тема, спикеры; выход: план; роли: маркетолог) → 2) Регистрация (вход: лендинг; выход: лиды; роли: маркетолог) → 3) Проведение (вход: материалы; выход: запись; роли: спикер) → 4) Follow-up (вход: список лидов; выход: письма; роли: CRM-менеджер) → 5) Аналитика (вход: посещаемость; выход: отчет; роли: аналитик) | 1) План (Notion) 2) Лидогенерация (Tilda/HubSpot) 3) Вебинар (Zoom/Teams) 4) Follow-up (CRM/ESP) 5) Аналитика (GA4/BI) |
| Исследование рынка | 1) Формулировка гипотез (вход: цели; выход: гипотезы; роли: маркетолог) → 2) Сбор данных (вход: анкеты; выход: ответы; роли: исследователь) → 3) Анализ (вход: данные; выход: выводы; роли: аналитик) → 4) Рекомендации (вход: выводы; выход: план действий; роли: маркетолог) | 1) Гипотезы (Miro/Notion) 2) Опросы (Typeform/Google Forms) 3) Анализ (Excel/BI) 4) Рекомендации (Confluence) |

### Вертикаль: Продажи

| Сценарий | Pipeline (шаги → входы → выходы → роли) | Функции и приложения по шагам |
| --- | --- | --- |
| Лидогенерация | 1) Сбор лидов (вход: формы/списки; выход: лиды; роли: маркетолог) → 2) Квалификация (вход: лиды; выход: SQL; роли: SDR) → 3) Назначение ответственного (вход: SQL; выход: владелец; роли: руководитель) | 1) Формы (Tilda/HubSpot) 2) Квалификация (CRM) 3) Роутинг (CRM) |
| Демонстрация продукта | 1) Подготовка (вход: потребности; выход: сценарий демо; роли: sales) → 2) Проведение (вход: сценарий; выход: протокол; роли: sales) → 3) Follow-up (вход: протокол; выход: письмо/задачи; роли: sales) | 1) Подготовка (Notion) 2) Демо (Zoom/Meet) 3) Follow-up (CRM/Email) |
| Выставление КП | 1) Расчет (вход: требования; выход: коммерческое предложение; роли: sales) → 2) Согласование (вход: КП; выход: утвержденное КП; роли: руководитель) → 3) Отправка (вход: КП; выход: письмо; роли: sales) | 1) Конфигуратор цен (CPQ) 2) Согласование (Docflow) 3) Отправка (CRM/Email) |
| Работа с возражениями | 1) Фиксация возражений (вход: разговор; выход: список; роли: sales) → 2) Подбор аргументов (вход: база знаний; выход: ответы; роли: sales enablement) → 3) Коммуникация (вход: ответы; выход: решение клиента; роли: sales) | 1) Логирование (CRM) 2) База знаний (Confluence) 3) Коммуникации (Email/Телефония) |
| Закрытие сделки | 1) Согласование условий (вход: КП; выход: финальные условия; роли: sales) → 2) Подписание (вход: договор; выход: подписанный договор; роли: юрист, клиент) → 3) Передача в исполнение (вход: договор; выход: проект; роли: sales, delivery) | 1) Согласование (CRM) 2) ЭДО (DocuSign/Диадок) 3) Передача (Jira/PM) |

### Вертикаль: HR

| Сценарий | Pipeline (шаги → входы → выходы → роли) | Функции и приложения по шагам |
| --- | --- | --- |
| Подбор персонала | 1) Заявка на вакансию (вход: потребность; выход: заявка; роли: руководитель) → 2) Поиск (вход: вакансия; выход: кандидаты; роли: рекрутер) → 3) Отбор (вход: резюме; выход: shortlist; роли: рекрутер) → 4) Интервью (вход: shortlist; выход: оценка; роли: hiring manager) → 5) Оффер (вход: оценка; выход: предложение; роли: HR) | 1) Заявка (HRM) 2) Источники (LinkedIn/HH) 3) ATS (Huntflow/Greenhouse) 4) Интервью (Calendar/Zoom) 5) Оффер (Docflow/HRM) |
| Онбординг | 1) Подготовка (вход: оффер; выход: план; роли: HR) → 2) Доступы (вход: план; выход: аккаунты; роли: IT) → 3) Обучение (вход: материалы; выход: завершенные курсы; роли: сотрудник, L&D) → 4) Адаптация (вход: отзывы; выход: отчет; роли: HR) | 1) План (Notion/HRM) 2) IAM (Okta/AD) 3) LMS (Moodle) 4) Оценка (HRM/Surveys) |
| Оценка эффективности | 1) Постановка целей (вход: OKR; выход: цели; роли: руководитель) → 2) Сбор данных (вход: отчеты; выход: показатели; роли: аналитик) → 3) Ревью (вход: показатели; выход: оценка; роли: руководитель) → 4) Развитие (вход: оценка; выход: план развития; роли: HR) | 1) OKR (Workboard) 2) BI (Power BI) 3) Performance (Lattice) 4) План развития (HRM) |
| Обучение и развитие | 1) Выявление потребностей (вход: оценки; выход: потребности; роли: HR) → 2) План обучения (вход: потребности; выход: план; роли: L&D) → 3) Проведение (вход: курсы; выход: прохождение; роли: сотрудник) → 4) Оценка эффекта (вход: результаты; выход: отчет; роли: L&D) | 1) Опросы (SurveyMonkey) 2) План (LMS) 3) Курсы (LMS/Zoom) 4) Аналитика (LMS/BI) |
| Увольнение | 1) Инициирование (вход: решение; выход: заявка; роли: руководитель) → 2) Документы (вход: заявка; выход: документы; роли: HR/юрист) → 3) Offboarding (вход: список задач; выход: закрытие доступов; роли: IT) → 4) Интервью (вход: анкета; выход: отчет; роли: HR) | 1) Заявка (HRM) 2) Документооборот (Docflow) 3) IAM (Okta/AD) 4) Exit интервью (Forms/HRM) |

### Вертикаль: Документооборот

| Сценарий | Pipeline (шаги → входы → выходы → роли) | Функции и приложения по шагам |
| --- | --- | --- |
| Согласование договора | 1) Инициирование (вход: шаблон; выход: черновик; роли: инициатор) → 2) Юр. проверка (вход: черновик; выход: правки; роли: юрист) → 3) Визирование (вход: правки; выход: согласования; роли: руководители) → 4) Подписание (вход: финал; выход: подписанный документ; роли: подписанты) | 1) Шаблоны (Docflow) 2) Ревью (Docflow) 3) Визирование (Docflow) 4) ЭДО (DocuSign) |
| Счет-фактура | 1) Формирование (вход: данные сделки; выход: счет; роли: бухгалтер) → 2) Отправка (вход: счет; выход: отправленный счет; роли: бухгалтер) → 3) Получение оплаты (вход: выписка; выход: отметка; роли: бухгалтер) | 1) Бухгалтерия (1С) 2) ЭДО (Диадок) 3) Банковские выписки (Client-Bank) |
| Внутренние приказы | 1) Инициирование (вход: запрос; выход: проект приказа; роли: HR/руководитель) → 2) Согласование (вход: проект; выход: визы; роли: юрист/руководители) → 3) Подписание (вход: финал; выход: приказ; роли: директор) | 1) Шаблоны (Docflow) 2) Согласование (Docflow) 3) Подписание (ЭДО) |
| Управление архивом | 1) Индексация (вход: документы; выход: метаданные; роли: архивариус) → 2) Хранение (вход: метаданные; выход: архив; роли: архивариус) → 3) Поиск (вход: запрос; выход: документ; роли: сотрудник) | 1) OCR/скан (ABBYY) 2) Архив (ECM) 3) Поиск (ECM) |
| Акт выполненных работ | 1) Формирование (вход: данные услуги; выход: акт; роли: бухгалтер) → 2) Согласование (вход: акт; выход: подтверждение; роли: клиент) → 3) Подписание (вход: финал; выход: подписанный акт; роли: стороны) | 1) Шаблоны (Docflow) 2) Согласование (ЭДО) 3) Подписание (ЭДО) |

### Вертикаль: Поддержка клиентов

| Сценарий | Pipeline (шаги → входы → выходы → роли) | Функции и приложения по шагам |
| --- | --- | --- |
| Обработка тикета | 1) Регистрация (вход: обращение; выход: тикет; роли: клиент, оператор) → 2) Классификация (вход: тикет; выход: приоритет; роли: оператор) → 3) Решение (вход: тикет; выход: ответ; роли: инженер) → 4) Закрытие (вход: ответ; выход: закрытый тикет; роли: оператор) | 1) Service Desk (Zendesk/Jira Service) 2) Категоризация (Service Desk) 3) Решение (Knowledge Base) 4) Закрытие (Service Desk) |
| Чат-бот | 1) Настройка сценариев (вход: FAQ; выход: сценарии; роли: CX) → 2) Запуск (вход: сценарии; выход: бот; роли: инженер) → 3) Передача оператору (вход: сложные кейсы; выход: эскалация; роли: оператор) | 1) База знаний (Confluence) 2) Бот-платформа (Dialogflow) 3) Эскалация (Service Desk) |
| SLA-управление | 1) Определение SLA (вход: договор; выход: SLA-матрица; роли: менеджер) → 2) Мониторинг (вход: тикеты; выход: статус SLA; роли: аналитик) → 3) Отчет (вход: статус; выход: отчет; роли: менеджер) | 1) SLA-матрица (Service Desk) 2) Мониторинг (BI) 3) Отчет (BI/Service Desk) |
| База знаний | 1) Сбор контента (вход: решения; выход: статьи; роли: эксперт) → 2) Публикация (вход: статьи; выход: база знаний; роли: контент-менеджер) → 3) Актуализация (вход: отзывы; выход: обновления; роли: эксперт) | 1) Документирование (Confluence) 2) Публикация (KB) 3) Ревизии (KB) |
| Управление инцидентами | 1) Обнаружение (вход: мониторинг; выход: инцидент; роли: NOC) → 2) Диагностика (вход: инцидент; выход: причина; роли: инженер) → 3) Восстановление (вход: план; выход: сервис восстановлен; роли: инженер) → 4) Постмортем (вход: данные; выход: отчет; роли: SRE) | 1) Мониторинг (Grafana) 2) Диагностика (Logs/APM) 3) Восстановление (Runbooks) 4) Постмортем (Confluence) |

### Вертикаль: Финансы

| Сценарий | Pipeline (шаги → входы → выходы → роли) | Функции и приложения по шагам |
| --- | --- | --- |
| Бюджетирование | 1) Сбор заявок (вход: заявки; выход: проект бюджета; роли: фин. аналитик) → 2) Согласование (вход: проект; выход: утвержденный бюджет; роли: CFO) → 3) Контроль (вход: факт; выход: отчет об отклонениях; роли: аналитик) | 1) Сбор (Excel/BI) 2) Согласование (ERP) 3) Контроль (BI) |
| Казначейство | 1) План платежей (вход: заявки; выход: календарь; роли: казначей) → 2) Проведение (вход: календарь; выход: платежи; роли: бухгалтер) → 3) Сверка (вход: выписка; выход: подтверждение; роли: бухгалтер) | 1) План (ERP) 2) Платежи (Client-Bank) 3) Сверка (ERP) |
| Управление дебиторкой | 1) Мониторинг (вход: счета; выход: список должников; роли: бухгалтер) → 2) Коммуникации (вход: список; выход: договоренности; роли: менеджер) → 3) Эскалация (вход: просрочка; выход: претензия; роли: юрист) | 1) Реестр (ERP/CRM) 2) Коммуникации (Email/CRM) 3) Претензии (Docflow) |
| Закрытие месяца | 1) Сбор данных (вход: первичка; выход: реестр; роли: бухгалтер) → 2) Проведение (вход: реестр; выход: проводки; роли: бухгалтер) → 3) Отчетность (вход: проводки; выход: отчет; роли: CFO) | 1) Реестр (ERP) 2) Проводки (ERP) 3) Отчетность (BI) |
| Управление затратами | 1) Сбор расходов (вход: заявки/чеки; выход: реестр; роли: бухгалтер) → 2) Контроль лимитов (вход: бюджет; выход: разрешения; роли: фин. контролер) → 3) Аналитика (вход: реестр; выход: отчет; роли: аналитик) | 1) Заявки (ERP) 2) Контроль (ERP) 3) Аналитика (BI) |

## 5. Матрица «функции ↔ сценарии»

| Функция | Маркетинг: кампании | Маркетинг: контент | Продажи: демо | HR: подбор | Документооборот: договоры | Поддержка: тикеты | Финансы: бюджет |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Сбор требований/бриф | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| Планирование/календарь | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |
| Управление задачами | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Документооборот/ЭДО |  |  | ✓ | ✓ | ✓ |  | ✓ |
| Коммуникации (email/чат/звонки) | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| Аналитика/отчетность | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Хранилище знаний | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Интеграции/автоматизация | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## 6. Схемы/таблицы сценариев (сводные)

### Сценарий: Запуск рекламной кампании (схема)

1) Бриф → 2) Планирование → 3) Настройка → 4) Оптимизация → 5) Отчет

### Сценарий: Подбор персонала (таблица)

| Шаг | Входы | Выходы | Роли | Приложения |
| --- | --- | --- | --- | --- |
| Заявка на вакансию | Потребность | Заявка | Руководитель | HRM |
| Поиск кандидатов | Вакансия | Кандидаты | Рекрутер | LinkedIn/HH |
| Отбор | Резюме | Shortlist | Рекрутер | ATS |
| Интервью | Shortlist | Оценка | Hiring manager | Calendar/Zoom |
| Оффер | Оценка | Оффер | HR | Docflow/HRM |
Набор материалов для проектирования и документирования макросов.

## Содержимое

- `docs/macros/spec.md` — спецификация формата макроса.
- `docs/macros/guide.md` — руководство по использованию.
- `schemas/macro.schema.json` — схема валидации.
- `templates/macros.yaml` — набор шаблонов макросов.

## Планы и организационные документы

- `plans/plan-raci.md` — роли и RACI-матрица по этапам.
- `plans/plan-dod.md` — план согласования и Definition of Done.
- `plans/plan-roadmap.md` — план работ, оценки длительности и риски.
- `plans/plan-prototype.md` — план прототипирования и ключевые экраны.
- `plans/plan-session.md` — план сессии и рабочие договоренности.
- `plans/plan-timeline.md` — таймлайн проекта и ключевые даты.

## Архив README

- `readmes/README-index.md` — индекс версий README.md из истории репозитория.
## Отзывы и рекомендации

### 1. Разделение оценок
- **Оценка качества**: соответствует ли артефакт заявленным требованиям, работает ли стабильно, корректно ли описан.
- **Оценка полезности**: насколько артефакт помог решить задачу пользователя, сэкономил время или улучшил результат.
- Оценки собираются раздельно, чтобы отличать объективную стабильность от субъективной пользы.

### 2. Привязка отзывов к подтвержденному использованию
- Отзыв можно оставить только после подтвержденного использования (лог события, подтвержденный запуск, отметка в системе).
- Отзыв помечается как **verified** и используется в расчетах рейтинга/рекомендаций.
- Неподтвержденные отзывы сохраняются отдельно и не влияют на итоговые статусы.

### 3. Статус зрелости
Статусы отражают готовность и надежность артефакта:
- **Прототип** — экспериментальный, возможны критические ограничения.
- **Стабильное** — проверен на практике, ограниченное количество дефектов.
- **Рекомендовано** — доказанная надежность и полезность, подтвержденные метриками.

### 4. Алгоритм ранжирования по сценариям
- Рейтинг считается отдельно для каждого сценария использования.
- В расчет входят только подтвержденные отзывы (verified).
- Итоговый балл сценария: средняя оценка качества и полезности с учетом доли подтвержденных отзывов и штрафа за спам‑риск.
- Применяется коэффициент свежести для отзывов старше 12 месяцев.

### 5. Таблица метрик рейтинга

| Метрика | Описание | Использование |
| --- | --- | --- |
| `quality_score_avg` | Средняя оценка качества по подтвержденным отзывам | Итоговый балл и уровни зрелости |
| `utility_score_avg` | Средняя оценка полезности по подтвержденным отзывам | Итоговый балл и уровни зрелости |
| `verified_usage_ratio` | Доля подтвержденных отзывов | Доверительный бонус |
| `review_volume` | Количество подтвержденных отзывов | Порог допуска к ранжированию |
| `freshness_factor` | Коэффициент свежести | Корректировка баллов |
| `spam_risk_score` | Риск спама | Штраф к рейтингу и модерации |

### 6. Механизм модерации и анти-спама
- Автоматическая проверка на дубликаты и спам (повторяющийся текст, подозрительные паттерны).
- Ограничение частоты публикации отзывов от одного пользователя/организации.
- Ручная модерация спорных отзывов и возможность апелляции.
- Репутационные коэффициенты для пользователей с историей подтвержденных отзывов.

### 7. Критерии «рекомендаций» и «лидеров кластера»
- **Рекомендации** присваиваются при выполнении порогов:
  - Минимальное количество подтвержденных отзывов.
  - Средняя оценка качества и полезности выше заданного уровня.
  - Отсутствие критических дефектов за последний период.
- **Лидеры кластера** определяются по сочетанию:
  - Максимальный индекс полезности в своем кластере.
  - Стабильность качества на горизонте времени.
  - Уровень внедрения/использования по подтвержденным данным.
## 1. Структура макроса

**Стандартная структура:** триггер → шаги → условия → ошибки → результат.

- **Триггер** — событие или сигнал, который запускает выполнение.
  - Примеры: входящее письмо, изменение статуса, ручной запуск.
- **Шаги** — упорядоченный набор действий, которые выполняются после триггера.
  - Каждый шаг имеет тип действия и параметры.
- **Условия** — правила, ограничивающие выполнение макроса или отдельных шагов.
  - Примеры: фильтр по полям, проверка контекста, контроль времени.
- **Ошибки** — обработка исключительных ситуаций и политика повторов.
  - Примеры: ретраи, уведомления, альтернативные ветки.
- **Результат** — ожидаемый выход/эффект, статус выполнения и артефакты.
  - Примеры: созданная задача, отправленное уведомление, запись в журнал.

## 2. Единый формат хранения макросов (JSON) и схема валидации

**Выбран формат хранения:** JSON (канонический).  
**Схема валидации:** JSON Schema Draft 2020-12 (`docs/macro_schema.json`).

Для удобства авторинга допускается YAML, но перед сохранением в хранилище он должен быть
приведен к JSON и валидирован по схеме.

```json
{
  "id": "string",
  "name": "string",
  "version": "1.0",
  "description": "string",
  "parameters": {
    "param_name": {
      "type": "string|number|boolean|array|object",
      "default": "value",
      "required": false,
      "description": "string"
    }
  },
  "trigger": {
    "type": "string",
    "params": {
      "use_parameters": true
    }
  },
  "steps": [
    {
      "id": "string",
      "type": "string",
      "params": {
        "use_parameters": true
      },
      "conditions": [
        {
          "type": "string",
          "params": {
            "use_parameters": true
          }
        }
      ],
      "on_error": {
        "strategy": "retry|skip|abort|fallback",
        "retries": 0,
        "fallback_step_id": "string"
      }
    }
  ],
  "conditions": [
    {
      "type": "string",
      "params": {
        "use_parameters": true
      }
    }
  ],
  "errors": {
    "default_strategy": "retry|skip|abort",
    "notify": ["email", "slack", "webhook"],
    "log_level": "info|warn|error"
  },
  "result": {
    "status": "success|partial|failed",
    "outputs": {}
  },
  "metadata": {
    "tags": ["string"],
    "owner": "string",
    "created_at": "ISO-8601",
    "updated_at": "ISO-8601"
  }
}
```

## 3. Базовые макросы (10–20 популярных сценариев)

Ниже — 12 базовых макросов в предложенном JSON-формате (сокращённо, без служебных полей).

### 3.1. Автоответ на входящее письмо
```json
{
  "id": "macro-auto-reply",
  "name": "Автоответ клиенту",
  "trigger": {"type": "email_received", "params": {"mailbox": "support@"}},
  "steps": [
    {"id": "send-reply", "type": "send_email", "params": {"template": "auto_reply"}}
  ],
  "conditions": [{"type": "subject_contains", "params": {"value": "заявка"}}],
  "errors": {"default_strategy": "retry", "notify": ["email"], "log_level": "warn"},
  "result": {"status": "success"}
}
```

### 3.2. Создание задачи из письма
```json
{
  "id": "macro-email-to-task",
  "name": "Письмо → задача",
  "trigger": {"type": "email_received", "params": {"mailbox": "support@"}},
  "steps": [
    {"id": "create-task", "type": "create_task", "params": {"project": "Support"}}
  ],
  "conditions": [{"type": "sender_domain", "params": {"value": "customer.com"}}],
  "errors": {"default_strategy": "retry", "notify": ["slack"], "log_level": "error"},
  "result": {"status": "success"}
}
```

### 3.3. Назначение ответственного при новом тикете
```json
{
  "id": "macro-assign-agent",
  "name": "Автоназначение ответственного",
  "trigger": {"type": "ticket_created", "params": {"queue": "L1"}},
  "steps": [
    {"id": "assign", "type": "assign_user", "params": {"strategy": "round_robin"}}
  ],
  "conditions": [{"type": "priority_in", "params": {"values": ["low", "normal"]}}],
  "errors": {"default_strategy": "skip", "notify": ["slack"], "log_level": "warn"},
  "result": {"status": "success"}
}
```

### 3.4. Эскалация при просрочке SLA
```json
{
  "id": "macro-sla-escalation",
  "name": "Эскалация SLA",
  "trigger": {"type": "sla_breached", "params": {"threshold": "15m"}},
  "steps": [
    {"id": "notify", "type": "notify", "params": {"channel": "slack", "room": "#oncall"}}
  ],
  "conditions": [{"type": "ticket_status", "params": {"value": "open"}}],
  "errors": {"default_strategy": "retry", "notify": ["email"], "log_level": "error"},
  "result": {"status": "success"}
}
```

### 3.5. Обновление статуса по завершению задачи
```json
{
  "id": "macro-close-ticket",
  "name": "Закрытие тикета при решении",
  "trigger": {"type": "task_completed", "params": {"project": "Support"}},
  "steps": [
    {"id": "update", "type": "update_ticket", "params": {"status": "closed"}}
  ],
  "conditions": [{"type": "resolution_code", "params": {"value": "solved"}}],
  "errors": {"default_strategy": "retry", "notify": ["slack"], "log_level": "warn"},
  "result": {"status": "success"}
}
```

### 3.6. Синхронизация контакта с CRM
```json
{
  "id": "macro-crm-sync",
  "name": "Синхронизация контакта",
  "trigger": {"type": "contact_updated", "params": {"source": "support"}},
  "steps": [
    {"id": "sync", "type": "upsert_crm_contact", "params": {"crm": "HubSpot"}}
  ],
  "conditions": [{"type": "field_changed", "params": {"value": "email"}}],
  "errors": {"default_strategy": "retry", "notify": ["email"], "log_level": "error"},
  "result": {"status": "success"}
}
```

### 3.7. Напоминание о необработанном тикете
```json
{
  "id": "macro-idle-reminder",
  "name": "Напоминание о простое",
  "trigger": {"type": "ticket_idle", "params": {"duration": "2h"}},
  "steps": [
    {"id": "remind", "type": "notify", "params": {"channel": "email", "template": "idle_reminder"}}
  ],
  "conditions": [{"type": "assignee_exists", "params": {"value": true}}],
  "errors": {"default_strategy": "skip", "notify": ["email"], "log_level": "warn"},
  "result": {"status": "success"}
}
```

### 3.8. Выставление счета после закрытия
```json
{
  "id": "macro-invoice-on-close",
  "name": "Счет после закрытия",
  "trigger": {"type": "ticket_closed", "params": {"queue": "Billing"}},
  "steps": [
    {"id": "invoice", "type": "create_invoice", "params": {"template": "standard"}}
  ],
  "conditions": [{"type": "tag_contains", "params": {"value": "billable"}}],
  "errors": {"default_strategy": "retry", "notify": ["email"], "log_level": "error"},
  "result": {"status": "success"}
}
```

### 3.9. Доставка отчета по расписанию
```json
{
  "id": "macro-report-delivery",
  "name": "Отчет по расписанию",
  "trigger": {"type": "schedule", "params": {"cron": "0 9 * * 1"}},
  "steps": [
    {"id": "run-report", "type": "run_report", "params": {"template": "weekly"}},
    {"id": "notify", "type": "notify", "params": {"channel": "email", "template": "report_ready"}}
  ],
  "conditions": [{"type": "timezone_in", "params": {"values": ["Europe/Moscow"]}}],
  "errors": {"default_strategy": "retry", "notify": ["email"], "log_level": "warn"},
  "result": {"status": "success"}
}
```

### 3.10. Дедупликация лидов
```json
{
  "id": "macro-lead-dedup",
  "name": "Дедупликация лидов",
  "trigger": {"type": "lead_created", "params": {"source": "forms"}},
  "steps": [
    {"id": "find-duplicates", "type": "find_duplicates", "params": {"key": "email"}},
    {"id": "merge", "type": "merge_leads", "params": {"strategy": "latest"}}
  ],
  "conditions": [{"type": "duplicates_found", "params": {"min_count": 1}}],
  "errors": {"default_strategy": "skip", "notify": ["slack"], "log_level": "warn"},
  "result": {"status": "success"}
}
```

### 3.11. Продление подписки
```json
{
  "id": "macro-renewal-reminder",
  "name": "Напоминание о продлении",
  "trigger": {"type": "subscription_expiring", "params": {"days_before": 7}},
  "steps": [
    {"id": "notify", "type": "notify", "params": {"channel": "email", "template": "renewal_notice"}}
  ],
  "conditions": [{"type": "plan_in", "params": {"values": ["pro", "enterprise"]}}],
  "errors": {"default_strategy": "retry", "notify": ["email"], "log_level": "warn"},
  "result": {"status": "success"}
}
```

### 3.12. Контроль возвратов
```json
{
  "id": "macro-refund-approval",
  "name": "Согласование возврата",
  "trigger": {"type": "refund_requested", "params": {"channel": "web"}},
  "steps": [
    {"id": "check", "type": "fraud_check", "params": {"threshold": 0.7}},
    {"id": "approve", "type": "approve_refund", "params": {"strategy": "manager"}}
  ],
  "conditions": [{"type": "amount_lt", "params": {"value": 1000}}],
  "errors": {"default_strategy": "fallback", "notify": ["slack"], "log_level": "error"},
  "result": {"status": "success"}
}
```

## 4. Параметризация (что пользователь меняет без кода)

Пользователь настраивает макросы через блок `parameters` и подстановку значений в `trigger/steps/conditions`.

**Типовые параметры:**
- Каналы и получатели уведомлений (`email`, `slack`, `webhook`).
- Шаблоны сообщений и отчётов (`template`).
- Тайминги и расписания (`cron`, `days_before`, `duration`).
- Фильтры и сегменты (`queue`, `plan_in`, `tag_contains`).
- Политики ошибок (`default_strategy`, `retries`, `notify`).
- Метаданные для поиска (`tags`, `owner`, `priority`).

**Правило:** любые настройки, не требующие кода, должны быть выражены параметрами, а не
зашиты в типы шагов.

## 5. Рекомендации по автоматическому подбору макросов

- **Классифицируйте входящие события** по типам (почта, тикеты, CRM, биллинг), чтобы быстро сузить набор подходящих макросов.
- **Используйте веса и теги**: каждому макросу задайте теги и приоритеты. Ранжирование по совпадению тегов и истории успешных срабатываний.
- **Учитывайте контекст**: отдел, роль, время суток, регион, приоритет обращения — это повышает точность подбора.
- **Добавьте «обучение от выбора»**: сохраняйте, какие макросы выбирают сотрудники, и постепенно поднимайте их рейтинг.
- **Фильтруйте по условиям**: сначала отсекайте несовместимые макросы (условия), затем выбирайте лучший по скору.

## 6. Метрики качества макроса

- **Время настройки**
  - Среднее время от создания до первого успешного запуска (минуты/часы).
  - Количество итераций правок до стабильной работы.
- **Надежность**
  - Доля успешных запусков (Success Rate).
  - Частота ошибок по типам (ошибки триггеров, шагов, интеграций).
  - Среднее число ретраев на 1 запуск.
- **Эффективность**
  - Снижение ручных операций (в минутах/задачах).
  - Влияние на SLA (сокращение просрочек).
- **Полезность**
  - Частота использования макроса.
  - Оценка пользователей (CSAT/внутренние оценки).

## 7. Инструкции по применению и настройке

1. **Выберите макрос** из списка или каталога макросов и скопируйте JSON-шаблон.
2. **Заполните `parameters`** (значения без кода: каналы, фильтры, расписания).
3. **Подставьте параметры** в `trigger/steps/conditions` через `params`.
4. **Проверьте схему**: валидируйте JSON по `docs/macro_schema.json`.
5. **Зарегистрируйте макрос** в хранилище (например, `macros/` или БД).
6. **Запустите тестовый прогон** (dry-run) и проверьте логи `errors`/`result`.
7. **Включите мониторинг** успешности и обновляйте параметры по метрикам.
## Карты бизнес‑сценариев

Ниже представлены 10 ключевых бизнес‑сценариев с типовыми pipeline, привязкой функций/приложений и запасными ветками.

### 1) Лидогенерация и квалификация
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Сбор лидов | Формы, лендинги, источники трафика | Landing page, формы CRM | Google Forms, Tilda |
| 2. Обогащение | Карточка лида, контакты | Clearbit, CRM enrichment | Hunter, Snov.io |
| 3. Скоринг | Оценка лида, сегмент | Lead scoring CRM | Custom scoring в BI |
| 4. Передача в продажу | MQL/SQL, SLA | CRM workflow | Email‑триаж |

### 2) Продажи (воронка и сделки)
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Контакт | Запись звонка, notes | CRM, телефония | Google Sheets + VoIP |
| 2. Коммерческое предложение | КП, прайс | CPQ, Docs | Шаблоны в Docs |
| 3. Переговоры | История коммуникаций | CRM, email | Почта + календарь |
| 4. Закрытие сделки | Счет, договор | e‑Signature, ERP | PDF + ручная подпись |

### 3) Маркетинг‑контент (контент‑поток)
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Планирование | Контент‑календарь | Notion/Asana | Google Sheets |
| 2. Производство | Черновики, ассеты | Docs, Figma | Canva, Miro |
| 3. Ревью/согласование | Комментарии, правки | Workflow/Approvals | Email + Docs |
| 4. Публикация | Посты, ссылки | CMS, SMM | Buffer, Hootsuite |

### 4) Клиентская поддержка
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Прием обращения | Тикет, категория | Helpdesk | Email‑ящик |
| 2. Классификация | Теги, приоритет | Автотеггинг | Ручная сортировка |
| 3. Решение | Ответ, база знаний | KB + макросы | FAQ в Docs |
| 4. Закрытие/CSAT | Оценка, отчеты | CSAT/NPS | Опросник Forms |

### 5) Онбординг клиента
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Подготовка | План внедрения | PM‑система | Таблица + чеклист |
| 2. Конфигурация | Настройки, доступы | IAM, Product setup | Ручная настройка |
| 3. Обучение | Гайды, записи | LMS, вебинары | Видео + Docs |
| 4. Go‑Live | Акт запуска, SLA | CRM/CSM | Email‑подтверждение |

### 6) Бухгалтерия и финансы
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Выставление счетов | Счета, акты | ERP/Accounting | Шаблоны PDF |
| 2. Платежи | Выписки, платежки | Bank API | Ручная загрузка |
| 3. Сверка | Реестр платежей | Reconciliation | Табличная сверка |
| 4. Отчетность | Баланс, P&L | BI/Accounting | Экспорт в Excel |

### 7) Логистика и доставка
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Формирование заказа | Order ID, накладная | OMS/WMS | Google Sheets |
| 2. Подбор/упаковка | Сборочный лист | WMS | Ручной лист |
| 3. Отгрузка | ТТН, трек‑номер | 3PL/Carrier API | Ручная заявка |
| 4. Доставка/подтверждение | POD, статус | TMS/Tracking | Email/звонок |

### 8) HR‑рекрутинг
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Поиск кандидатов | Воронка, CV | ATS | Google Sheets |
| 2. Скрининг | Notes, scorecard | ATS + календарь | Email + Docs |
| 3. Интервью | Записи, фидбек | Zoom/Meet | Телефон |
| 4. Оффер | Offer letter | HRIS/e‑Sign | PDF + подпись |

### 9) Управление продуктом и разработкой
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Сбор требований | PRD, backlog | Jira/Confluence | Notion |
| 2. Планирование | Roadmap, спринт | Jira | Trello |
| 3. Разработка | Код, MR/PR | Git, CI | Патч‑процесс |
| 4. Релиз | Release notes | CI/CD | Ручной деплой |

### 10) Аналитика и отчетность
| Шаг | Артефакты | Основные функции/приложения | Запасные ветки |
| --- | --- | --- | --- |
| 1. Сбор данных | Логи, события | ETL/ELT | CSV‑экспорт |
| 2. Хранилище | DWH, витрины | BigQuery/Snowflake | Postgres |
| 3. Анализ | Метрики, дашборды | BI | Google Data Studio |
| 4. Рассылка | Отчеты, алерты | Slack/Email alerts | Ручная рассылка |
## Цель
Метаслой для поиска, интеграции и повторного использования готовых решений.

## Глоссарий: базовые категории функций
- **Ввод данных** — получение данных из форм, API, файлов, веб-скрейпинга, датчиков.
- **Вывод данных** — отображение, экспорт, отправка в сторонние системы.
- **Трансформация** — очистка, нормализация, обогащение, сопоставление, агрегация.
- **Хранение** — базы данных, файлы, облачные хранилища, кэши.
- **Уведомления** — email, мессенджеры, вебхуки, push.
- **Аналитика** — отчёты, дашборды, метрики, прогнозирование.
- **Оркестрация** — очереди, расписания, триггеры, пайплайны.
- **Безопасность** — доступы, аудит, шифрование, комплаенс.

## Минимальный паспорт функции
- **Название**
- **Назначение/описание**
- **Входы** (формат, обязательность, ограничения)
- **Выходы** (формат, гарантии)
- **Условия выполнения** (триггеры, зависимости)
- **Ограничения** (лимиты, квоты, SLA)
- **Цена** (стоимость за запуск/месяц, фримиум)
- **Уровень зрелости** (MVP/бета/прод)
- **Пример использования**

## Примеры
- **WordPress‑плагины**: формы, SEO, кеширование, интеграции CRM.
- **Make.com‑сценарии**: автоматизация заявок, синхронизация таблиц и CRM, рассылки.
- **SaaS‑модули**: биллинг, аналитика, уведомления, авторизация.

## Словник (MVP, 10–20 функций)
1. **Сбор данных из форм** — принимать ввод с сайта и сохранять в таблицу/CRM.
2. **Импорт CSV** — загрузка и валидация табличных данных.
3. **Экспорт CSV/XLSX** — выгрузка данных по фильтрам.
4. **Вебхук‑приёмник** — приём событий от внешних систем.
5. **Вебхук‑отправитель** — отправка событий в внешние сервисы.
6. **Очистка данных** — удаление дублей, нормализация форматов.
7. **Сопоставление сущностей** — связывание контактов/компаний/заказов.
8. **Обогащение данных** — добавление сведений из внешних API.
9. **Планировщик задач** — запуск по расписанию/CRON.
10. **Очередь задач** — асинхронная обработка запросов.
11. **Уведомление email** — шаблоны писем и рассылка.
12. **Уведомление в мессенджер** — Slack/Telegram/Teams.
13. **Хранение файлов** — загрузка и доступ к документам.
14. **Хранение данных** — таблица/БД для сущностей.
15. **Дашборд метрик** — базовая аналитика по событиям.
16. **Отчёт по KPI** — периодическая агрегация и выгрузка.
17. **Авторизация** — логин/SSO/ролевая модель.
18. **Биллинг** — подписки, счета, оплатa.
