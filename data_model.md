# Схема сущностей и отношений

## 1. Поля сущностей

Ниже приведён базовый набор полей для всех доменных сущностей (например, `Module`, `Function`, `UseCase`, `Macro`, `Component`, `Service` и т.п.).

| Поле | Тип | Обязательное | Описание |
|---|---|---|---|
| `id` | UUID (v4) | да | Уникальный идентификатор сущности. |
| `name` | String (1–255) | да | Человекочитаемое имя. Должно быть уникально в рамках типа сущности. |
| `description` | Text | нет | Подробное описание. |
| `metadata` | JSONB / Map<String, Any> | нет | Дополнительные атрибуты, не влияющие на логику (теги, ссылки, авторы и т.п.). |
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
