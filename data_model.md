# Схема сущностей и отношений

## 1. Поля сущностей

Ниже приведён базовый набор полей для всех доменных сущностей (например, `Module`, `Function`, `UseCase`, `Macro`, `Review`, `Rating` и т.п.).

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `id` | UUID (v4) | да | Уникальный идентификатор сущности. |
| `name` | String (1–255) | да | Человекочитаемое имя. Должно быть уникально в рамках типа сущности. |
| `description` | Text | нет | Подробное описание. |
| `metadata` | JSONB / Map<String, Any> | нет | Дополнительные атрибуты, не влияющие на логику (теги, ссылки, авторы и т.п.). |
| `maturity` | Enum (Prototype, Stable, Recommended) | нет | Уровень зрелости для каталогов сценариев/приложений. |
| `version` | Integer | да | Номер версии сущности, увеличивается при изменениях. |
| `created_at` | Timestamp (UTC) | да | Время создания записи. |
| `updated_at` | Timestamp (UTC) | да | Время последнего изменения записи. |
| `version` | Integer | да | Номер версии для оптимистической блокировки. |

## 1.1 Спецификация ключевых сущностей

### Function
- Назначение: единица реализуемой бизнес-логики/кода.
- Доп. поля: `signature` (String), `return_type` (String), `visibility` (enum: public/internal/private), `language` (String).

### Module
- Назначение: группировка функций и макросов.
- Доп. поля: `owner_team` (String), `domain` (String).

### UseCase
- Назначение: пользовательский сценарий/функциональное требование.
- Доп. поля: `status` (enum: draft/active/deprecated), `priority` (enum: low/medium/high/critical).

### Macro
- Назначение: составная операция/шаблон, используемый в нескольких UseCase.
- Доп. поля: `kind` (enum: script/pipeline/rule), `inputs` (JSON), `outputs` (JSON).

### Review
- Назначение: экспертная оценка сущности (Function/Module/UseCase/Macro).
- Доп. поля: `subject_type` (enum), `subject_id` (UUID), `author_id` (UUID), `text` (Text), `status` (enum: open/closed).

### Rating
- Назначение: числовая оценка сущности.
- Доп. поля: `subject_type` (enum), `subject_id` (UUID), `author_id` (UUID), `score` (Integer 1–5).

Дополнительно для всех версионируемых сущностей:

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `version` | SemVer String | да | Версия в формате `MAJOR.MINOR.PATCH`. |
| `revision` | Integer | да | Последовательная ревизия для истории изменений. |
| `effective_at` | Timestamp (UTC) | да | Дата/время вступления версии в силу. |
| `status` | Enum | да | Состояние (`draft`, `active`, `deprecated`). |

### 1.1. Доменные сущности и их специфические поля

**`Function`**
- `signature` (String, optional) — публичная сигнатура/контракт.
- `module_ids` (UUID[]) — ссылки на модули, где используется функция.

**`Module`**
- `owner` (String, optional) — ответственная команда/роль.
- `function_ids` (UUID[]) — список функций, входящих в модуль.

**`UseCase`**
- `module_ids` (UUID[]) — модули, участвующие в сценарии.
- `function_ids` (UUID[]) — функции, которые выполняют сценарий.

**`Macro`**
- `use_case_ids` (UUID[]) — сценарии, которые объединяет макрос.

**`Review`**
- `target_type` (Enum: `function`, `module`, `use_case`, `macro`) — тип сущности, которую оценивают.
- `target_id` (UUID) — идентификатор целевой сущности.
- `author` (String, optional) — автор/роль ревью.
- `rating_id` (UUID) — ссылка на сущность `Rating`.
- `comment` (Text, optional) — текст отзыва.

**`Rating`**
- `score` (Integer) — оценка, например 1–5.
- `scale` (String, optional) — описание шкалы (например, `1-5`).
- `label` (String, optional) — человекочитаемая метка оценки (например, `good`).

## 1.1 Сущности отзывов и модерации

### `review`

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `id` | UUID (v4) | да | Идентификатор отзыва. |
| `entity_type` | String | да | Тип объекта отзыва. |
| `entity_id` | UUID (v4) | да | Идентификатор объекта. |
| `author_id` | UUID (v4) | да | Автор отзыва. |
| `rating` | Number | да | Оценка (например, 1–5). |
| `text` | Text | нет | Текст отзыва. |
| `status` | Enum | да | `pending`, `approved`, `rejected`. |
| `fraud_score` | Number | нет | Риск-скор (0–1). |
| `created_at` | Timestamp (UTC) | да | Время создания. |
| `updated_at` | Timestamp (UTC) | да | Время обновления. |

### `moderation_queue`

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `id` | UUID (v4) | да | Идентификатор очереди. |
| `review_id` | UUID (v4) | да | Ссылка на отзыв. |
| `reason` | Text | да | Причина постановки в очередь. |
| `status` | Enum | да | `open`, `in_review`, `resolved`. |
| `created_at` | Timestamp (UTC) | да | Время создания. |

### `moderation_decision`

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `id` | UUID (v4) | да | Идентификатор решения. |
| `review_id` | UUID (v4) | да | Ссылка на отзыв. |
| `moderator_id` | UUID (v4) | да | Модератор. |
| `decision` | Enum | да | `approved`, `rejected`. |
| `note` | Text | нет | Комментарий модератора. |
| `created_at` | Timestamp (UTC) | да | Время решения. |

### `fraud_signal`

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `id` | UUID (v4) | да | Идентификатор сигнала. |
| `review_id` | UUID (v4) | да | Ссылка на отзыв. |
| `signal_type` | String | да | Тип сигнала (frequency, pattern, repeat, ip_device). |
| `score` | Number | да | Вес сигнала. |
| `metadata` | JSONB | нет | Детали (IP, device, шаблон и т.п.). |

## 2. Связи между сущностями

### Примеры ключевых связей

- **`Function` ↔ `Module`**
  - Тип: многие-ко-многим (M:N)
  - Интерпретация: функция может принадлежать нескольким модулям, модуль содержит множество функций.
  - Реализация: таблица/ребро `module_function`.

- **`UseCase` ↔ `Macro`**
  - Тип: многие-ко-многим (M:N)
  - Интерпретация: use case может быть реализован несколькими macro, и macro может участвовать в нескольких use case.
  - Реализация: таблица/ребро `usecase_macro`.

- **`Review` → `Rating`**
  - Тип: один-ко-одному (1:1)
  - Интерпретация: отзыв использует ровно одну оценку.
  - Реализация: внешний ключ `rating_id` в `reviews`.

- **`Review` → (`Function`/`Module`/`UseCase`/`Macro`)**
  - Тип: многие-к-одному (M:1) через `target_type` + `target_id`.
  - Интерпретация: отзыв относится к одной целевой сущности.
  - Реализация: полиморфная связь либо отдельные таблицы связей.

### Дополнительные типовые связи (опционально)

- **`Module` ↔ `Component`**: один-ко-многим (1:N)
- **`Service` ↔ `UseCase`**: один-ко-многим (1:N)
- **`Function` ↔ `Function`**: многие-ко-многим (M:N) для зависимостей/вызовов

### Дополнительные связи для Review/Rating

- **`Review` → `Function/Module/UseCase/Macro`**
  - Тип: многие-ко-одному (N:1)
  - Интерпретация: отзыв относится к одной сущности, сущность может иметь много отзывов.
- **`Rating` → `Function/Module/UseCase/Macro`**
  - Тип: многие-ко-одному (N:1)
  - Интерпретация: оценка относится к одной сущности, сущность может иметь много оценок.

## 2.1 Таблица «Сущность → Поля → Связи»

| Сущность | Поля (помимо базовых) | Связи |
|---|---|---|
| Function | `signature`, `return_type`, `visibility`, `language` | M:N с Module; M:N с Function (dependencies); 1:N с Review/Rating |
| Module | `owner_team`, `domain` | M:N с Function; 1:N с Review/Rating |
| UseCase | `status`, `priority` | M:N с Macro; 1:N с Review/Rating |
| Macro | `kind`, `inputs`, `outputs` | M:N с UseCase; 1:N с Review/Rating |
| Review | `subject_type`, `subject_id`, `author_id`, `text`, `status` | N:1 к Function/Module/UseCase/Macro |
| Rating | `subject_type`, `subject_id`, `author_id`, `score` | N:1 к Function/Module/UseCase/Macro |

## 3. Ограничения

### Обязательность (NOT NULL)
- `id`, `name`, `version`, `created_at`, `updated_at` — обязательны для всех сущностей.
- `id`, `name`, `created_at`, `updated_at` — обязательны для всех сущностей.
- `version` — обязательна для всех сущностей.

### Уникальность
- `id` — глобально уникален.
- `name` — уникален **в пределах типа сущности** (например, два разных `Module` не могут иметь одинаковый `name`).
- Для связей M:N рекомендуется уникальный составной ключ (например, `(module_id, function_id)`), чтобы исключить дубликаты связей.

### Типы и валидация
- `id`: UUID v4.
- `name`: строка 1–255 символов, запрещены пустые строки.
- `description`: свободный текст.
- `metadata`: JSON-объект, допустимы только сериализуемые значения.
- `maturity`: перечисление `Prototype`, `Stable`, `Recommended` (если поле применимо).
- `version`: целое число >= 1.
- `created_at`, `updated_at`: UTC timestamps.

### Каскадные правила
- Удаление сущности должно удалять связи (CASCADE) либо блокироваться (RESTRICT) в зависимости от критичности данных.

## 4. Согласование со схемой хранения

### Выбранная модель: **гибридная (табличная + графовая)**

- **Табличная часть** хранит сущности и их поля (`id`, `name`, `description`, `metadata`, `created_at`, `updated_at`).
- **Графовая часть** хранит связи между сущностями (ребра M:N, зависимостей и т.п.).

#### Почему гибрид:
- Табличная модель удобна для CRUD и строгих ограничений.
- Графовая модель упрощает обход отношений (например, цепочки зависимостей `Function → Function` или связь `UseCase → Macro → Function`).

## 5. Черновик JSON-schema / OpenAPI (фрагменты)

Ниже — упрощённые фрагменты схем, пригодные для последующей сборки OpenAPI.

```json
{
  "components": {
    "schemas": {
      "BaseEntity": {
        "type": "object",
        "required": ["id", "name", "created_at", "updated_at", "version"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "name": { "type": "string", "minLength": 1, "maxLength": 255 },
          "description": { "type": "string" },
          "metadata": { "type": "object", "additionalProperties": true },
          "created_at": { "type": "string", "format": "date-time" },
          "updated_at": { "type": "string", "format": "date-time" },
          "version": { "type": "integer", "minimum": 1 }
        }
      },
      "Function": {
        "allOf": [
          { "$ref": "#/components/schemas/BaseEntity" },
          {
            "type": "object",
            "properties": {
              "signature": { "type": "string" },
              "return_type": { "type": "string" },
              "visibility": { "type": "string", "enum": ["public", "internal", "private"] },
              "language": { "type": "string" }
            }
          }
        ]
      },
      "Review": {
        "allOf": [
          { "$ref": "#/components/schemas/BaseEntity" },
          {
            "type": "object",
            "required": ["subject_type", "subject_id", "author_id", "status"],
            "properties": {
              "subject_type": { "type": "string", "enum": ["Function", "Module", "UseCase", "Macro"] },
              "subject_id": { "type": "string", "format": "uuid" },
              "author_id": { "type": "string", "format": "uuid" },
              "text": { "type": "string" },
              "status": { "type": "string", "enum": ["open", "closed"] }
            }
          }
        ]
      },
      "Rating": {
        "allOf": [
          { "$ref": "#/components/schemas/BaseEntity" },
          {
            "type": "object",
            "required": ["subject_type", "subject_id", "author_id", "score"],
            "properties": {
              "subject_type": { "type": "string", "enum": ["Function", "Module", "UseCase", "Macro"] },
              "subject_id": { "type": "string", "format": "uuid" },
              "author_id": { "type": "string", "format": "uuid" },
              "score": { "type": "integer", "minimum": 1, "maximum": 5 }
            }
          }
        ]
      }
    }
  }
}
```

## 6. Версионирование и история изменений

### Вариант хранения
- `version` увеличивается при каждом изменении сущности (оптимистическая блокировка).
- История хранится в таблицах вида `<entity>_history` с полями:
  - `id` (UUID), `entity_id` (UUID), `version` (Integer), `changed_at` (Timestamp),
    `changed_by` (UUID), `diff` (JSONB), `snapshot` (JSONB).

### Альтернатива (event sourcing)
- События вида `FunctionCreated`, `FunctionUpdated`, `RatingAdded` и т.п.
- Снимки состояния по необходимости для ускорения чтения.

## 7. Минимальный набор API-эндпоинтов

### CRUD сущностей
- `GET /functions`, `POST /functions`
- `GET /functions/{id}`, `PATCH /functions/{id}`, `DELETE /functions/{id}`
- Аналогично для `modules`, `use-cases`, `macros`, `reviews`, `ratings`

### Связи
- `POST /modules/{id}/functions` (привязать функцию)
- `DELETE /modules/{id}/functions/{function_id}` (отвязать функцию)
- `POST /use-cases/{id}/macros`
- `DELETE /use-cases/{id}/macros/{macro_id}`

### История
- `GET /functions/{id}/history`
- Аналогично для остальных сущностей

### Соответствие

- **Entities** → таблицы (например, `modules`, `functions`, `use_cases`, `macros`).
- **Relations** → отдельные таблицы связей (в RDBMS) **или** ребра (в графовой БД).
- `metadata` хранится в JSONB (PostgreSQL) или аналогичном типе в выбранной СУБД.

Если проект полностью табличный, связи M:N реализуются через join-таблицы; если полностью графовый — сущности становятся вершинами, а таблицы заменяются ребрами, ограничения реализуются на уровне приложений/валидации.

## 5. Назначение архитектуры данных

Архитектура данных описывает единый контракт для знаний о функционале системы: какие сущности существуют, как они связаны и какие ограничения действуют. Это позволяет унифицировать сбор данных (модули, функции, сценарии использования, макросы) и делать достоверные выборки для анализа, рекомендаций и контроля качества.

Также архитектура данных задаёт основу для масштабируемого хранения и последующих интеграций. Единые идентификаторы, типы и правила версионирования позволяют безопасно вносить изменения, сохранять историю и строить API без разночтений между командами и сервисами.

## 6. Выбор модели хранения

**Модель хранения: гибридная (табличная + графовая).**

- Табличная модель подходит для CRUD, уникальности и аналитики по сущностям.
- Графовая часть необходима для удобного обхода связей (например, `UseCase → Macro → Function`, зависимости функций, соответствие модулей и функций).

Таким образом, сущности живут в реляционных таблицах, а сложные связи фиксируются в таблицах-ребрах или в графовой СУБД, если понадобится быстрый traversal.

## 7. Сущности

Определены ключевые сущности домена:

- `Function`
- `Module`
- `UseCase`
- `Macro`
- `Review`
- `Rating`

## 8. Таблица «Сущность → поля → связи»

| Сущность | Поля | Связи |
|---|---|---|
| `Module` | `id`, `name`, `description`, `metadata`, `version`, `created_at`, `updated_at` | M:N с `Function` через `module_function` |
| `Function` | `id`, `name`, `description`, `metadata`, `version`, `created_at`, `updated_at` | M:N с `Module`; M:N с `UseCase` через `usecase_function`; M:N с `Function` (зависимости) |
| `UseCase` | `id`, `name`, `description`, `metadata`, `version`, `created_at`, `updated_at` | M:N с `Macro` через `usecase_macro`; M:N с `Function` через `usecase_function`; 1:N с `Review` |
| `Macro` | `id`, `name`, `description`, `metadata`, `version`, `created_at`, `updated_at` | M:N с `UseCase` через `usecase_macro` |
| `Review` | `id`, `use_case_id`, `author`, `summary`, `metadata`, `version`, `created_at`, `updated_at` | N:1 к `UseCase`; 1:N с `Rating` |
| `Rating` | `id`, `review_id`, `score`, `criteria`, `metadata`, `version`, `created_at`, `updated_at` | N:1 к `Review` |

## 9. Черновик JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/schemas/data-entities.json",
  "title": "Data Entities",
  "type": "object",
  "definitions": {
    "BaseEntity": {
      "type": "object",
      "properties": {
        "id": { "type": "string", "format": "uuid" },
        "name": { "type": "string", "minLength": 1, "maxLength": 255 },
        "description": { "type": "string" },
        "metadata": { "type": "object" },
        "version": { "type": "integer", "minimum": 1 },
        "created_at": { "type": "string", "format": "date-time" },
        "updated_at": { "type": "string", "format": "date-time" }
      },
      "required": ["id", "name", "version", "created_at", "updated_at"]
    },
    "Module": { "allOf": [{ "$ref": "#/definitions/BaseEntity" }] },
    "Function": { "allOf": [{ "$ref": "#/definitions/BaseEntity" }] },
    "UseCase": { "allOf": [{ "$ref": "#/definitions/BaseEntity" }] },
    "Macro": { "allOf": [{ "$ref": "#/definitions/BaseEntity" }] },
    "Review": {
      "allOf": [
        { "$ref": "#/definitions/BaseEntity" },
        {
          "type": "object",
          "properties": {
            "use_case_id": { "type": "string", "format": "uuid" },
            "author": { "type": "string", "minLength": 1 },
            "summary": { "type": "string" }
          },
          "required": ["use_case_id", "author"]
        }
      ]
    },
    "Rating": {
      "allOf": [
        { "$ref": "#/definitions/BaseEntity" },
        {
          "type": "object",
          "properties": {
            "review_id": { "type": "string", "format": "uuid" },
            "score": { "type": "number", "minimum": 0, "maximum": 5 },
            "criteria": { "type": "string" }
          },
          "required": ["review_id", "score"]
        }
      ]
    }
  }
}
```

## 10. Версионирование данных и история изменений

- Каждая сущность имеет поле `version` (целое, автоинкремент при изменениях) в таблице и сохраняется в таблице истории `entity_versions`.
- Таблица истории содержит: `entity_type`, `entity_id`, `version`, `changed_by`, `changed_at`, `change_summary`, `payload` (JSONB снимок).
- Для связей M:N хранится история в таблицах `*_history` (например, `module_function_history`) с полями `action` (add/remove), `changed_at`, `changed_by`.
- API поддерживает чтение версии через параметр `?version=` и восстановление по `POST /{entity}/{id}/restore`.

## 11. API чтения/записи и минимальные эндпоинты

**Стиль: REST (с возможным слоем GraphQL для чтения сложных графов).**

REST обеспечивает простые CRUD-операции и прозрачное кэширование. GraphQL может использоваться для выборок с глубокими связями (например, сценарий → макросы → функции) без множества запросов.

### Минимальный набор REST эндпоинтов

```
GET    /modules
POST   /modules
GET    /modules/{id}
PATCH  /modules/{id}
GET    /functions
POST   /functions
GET    /functions/{id}
PATCH  /functions/{id}
GET    /use-cases
POST   /use-cases
GET    /use-cases/{id}
PATCH  /use-cases/{id}
GET    /macros
POST   /macros
GET    /macros/{id}
PATCH  /macros/{id}
GET    /reviews
POST   /reviews
GET    /reviews/{id}
PATCH  /reviews/{id}
GET    /ratings
POST   /ratings
GET    /ratings/{id}
PATCH  /ratings/{id}
GET    /use-cases/{id}/reviews
GET    /reviews/{id}/ratings
GET    /{entity}/{id}/versions
POST   /{entity}/{id}/restore
```

### Черновик GraphQL (опционально)

```graphql
type Query {
  module(id: ID!): Module
  function(id: ID!): Function
  useCase(id: ID!): UseCase
  macro(id: ID!): Macro
}

type UseCase {
  id: ID!
  name: String!
  description: String
  macros: [Macro!]
  functions: [Function!]
  reviews: [Review!]
}
```
## 5. Отзывы и рейтинги

### 5.1. Сущность `review`

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `id` | UUID (v4) | да | Уникальный идентификатор отзыва. |
| `entity_type` | String | да | Тип сущности, к которой относится отзыв (`module`, `service`, `macro` и т.д.). |
| `entity_id` | UUID | да | Идентификатор сущности. |
| `author_id` | UUID | да | Пользователь, оставивший отзыв. |
| `quality_rating` | Integer (1–5) | да | Оценка качества (стабильность, соответствие стандартам). |
| `usefulness_rating` | Integer (1–5) | да | Оценка полезности (насколько помогает решить задачу). |
| `quality_comment` | Text | нет | Текстовое обоснование оценки качества. |
| `usefulness_comment` | Text | нет | Текстовое обоснование оценки полезности. |
| `legacy_rating` | Integer (1–5) | нет | Историческая одноосевая оценка (для миграции). |
| `legacy_rating_source` | String | нет | Маркер миграции: `split_default` / `legacy_only` / `manual_override`. |
| `status` | String | да | Статус отзыва (`pending`, `approved`, `rejected`). |
| `verified` | Boolean | да | Признак подтвержденного использования. |
| `verified_at` | Timestamp (UTC) | нет | Время последнего подтверждения использования. |
| `created_at` | Timestamp (UTC) | да | Время создания отзыва. |
| `updated_at` | Timestamp (UTC) | да | Время последнего обновления. |

### 5.2. Агрегаты рейтинга по сущности

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `entity_type` | String | да | Тип сущности. |
| `entity_id` | UUID | да | Идентификатор сущности. |
| `quality_avg` | Decimal(3,2) | да | Средняя оценка качества. |
| `usefulness_avg` | Decimal(3,2) | да | Средняя оценка полезности. |
| `quality_distribution` | JSONB | да | Распределение оценок качества (counts/percentiles). |
| `usefulness_distribution` | JSONB | да | Распределение оценок полезности (counts/percentiles). |
| `review_count` | Integer | да | Количество отзывов. |
| `verified_review_count` | Integer | да | Количество подтвержденных отзывов. |
| `updated_at` | Timestamp (UTC) | да | Время последнего пересчета агрегатов. |
## 5. Сущности отзывов и подтвержденного использования

### `review`

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| `id` | UUID (v4) | да | Уникальный идентификатор отзыва. |
| `user_id` | UUID (v4) | да | Автор отзыва. |
| `product_id` | UUID (v4) | да | Продукт/решение, на который оставлен отзыв. |
| `scenario_id` | UUID (v4) | да | Сценарий использования, к которому относится отзыв. |
| `quality_score` | Integer (1–5) | да | Оценка качества. |
| `utility_score` | Integer (1–5) | да | Оценка полезности. |
| `comment` | Text | да | Текст отзыва. |
| `verified_usage_id` | UUID (v4) | да | Ссылка на подтвержденное использование, использованное для валидации. |
| `status` | Enum | да | `pending` / `approved` / `rejected`. |
| `created_at` | Timestamp (UTC) | да | Время создания. |
| `updated_at` | Timestamp (UTC) | да | Время последнего изменения. |

### `verified_usage`

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| `id` | UUID (v4) | да | Идентификатор подтвержденного использования. |
| `user_id` | UUID (v4) | да | Пользователь, для которого подтверждено использование. |
| `product_id` | UUID (v4) | да | Продукт/решение. |
| `scenario_id` | UUID (v4) | да | Сценарий, для которого подтверждено использование. |
| `source` | String | да | Источник подтверждения (`sdk`, `integration`, `purchase`, `manual`). |
| `usage_count` | Integer | да | Количество подтвержденных запусков. |
| `verified_at` | Timestamp (UTC) | да | Дата последнего подтверждения. |
| `expires_at` | Timestamp (UTC) | да | Срок действия подтверждения. |
| `created_at` | Timestamp (UTC) | да | Время создания записи. |
| `updated_at` | Timestamp (UTC) | да | Время последнего изменения. |

### `verification_audit`

| Поле | Тип | Обязательное | Описание |
| --- | --- | --- | --- |
| `id` | UUID (v4) | да | Идентификатор записи аудита. |
| `verified_usage_id` | UUID (v4) | да | Связь с подтверждением. |
| `actor_id` | UUID (v4) | да | Кто подтвердил (пользователь, система или модератор). |
| `action` | String | да | Тип действия (`confirm`, `extend`, `revoke`). |
| `reason` | Text | нет | Причина/комментарий. |
| `created_at` | Timestamp (UTC) | да | Время фиксации действия. |
