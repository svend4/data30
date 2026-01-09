# Схема сущностей и отношений

## 1. Поля сущностей

Ниже приведён базовый набор полей для всех доменных сущностей (например, `Module`, `Function`, `UseCase`, `Macro`, `Component`, `Service` и т.п.).

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `id` | UUID (v4) | да | Уникальный идентификатор сущности. |
| `name` | String (1–255) | да | Человекочитаемое имя. Должно быть уникально в рамках типа сущности. |
| `description` | Text | нет | Подробное описание. |
| `metadata` | JSONB / Map<String, Any> | нет | Дополнительные атрибуты, не влияющие на логику (теги, ссылки, авторы и т.п.). |
| `version` | Integer | да | Номер версии сущности, увеличивается при изменениях. |
| `created_at` | Timestamp (UTC) | да | Время создания записи. |
| `updated_at` | Timestamp (UTC) | да | Время последнего изменения записи. |

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

### Дополнительные типовые связи (опционально)

- **`Module` ↔ `Component`**: один-ко-многим (1:N)
- **`Service` ↔ `UseCase`**: один-ко-многим (1:N)
- **`Function` ↔ `Function`**: многие-ко-многим (M:N) для зависимостей/вызовов

## 3. Ограничения

### Обязательность (NOT NULL)
- `id`, `name`, `version`, `created_at`, `updated_at` — обязательны для всех сущностей.

### Уникальность
- `id` — глобально уникален.
- `name` — уникален **в пределах типа сущности** (например, два разных `Module` не могут иметь одинаковый `name`).
- Для связей M:N рекомендуется уникальный составной ключ (например, `(module_id, function_id)`), чтобы исключить дубликаты связей.

### Типы и валидация
- `id`: UUID v4.
- `name`: строка 1–255 символов, запрещены пустые строки.
- `description`: свободный текст.
- `metadata`: JSON-объект, допустимы только сериализуемые значения.
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
