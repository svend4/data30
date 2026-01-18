# data30

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

## 2. Единый формат хранения макросов (JSON-шаблон)

```json
{
  "id": "string",
  "name": "string",
  "version": "1.0",
  "description": "string",
  "trigger": {
    "type": "string",
    "params": {}
  },
  "steps": [
    {
      "id": "string",
      "type": "string",
      "params": {},
      "conditions": [
        {
          "type": "string",
          "params": {}
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
      "params": {}
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

## 3. Базовые макросы (5–10 популярных сценариев)

Ниже — 8 базовых макросов в предложенном JSON-формате (сокращённо, без служебных полей).

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

## 4. Рекомендации по автоматическому подбору макросов

- **Классифицируйте входящие события** по типам (почта, тикеты, CRM, биллинг), чтобы быстро сузить набор подходящих макросов.
- **Используйте веса и теги**: каждому макросу задайте теги и приоритеты. Ранжирование по совпадению тегов и истории успешных срабатываний.
- **Учитывайте контекст**: отдел, роль, время суток, регион, приоритет обращения — это повышает точность подбора.
- **Добавьте «обучение от выбора»**: сохраняйте, какие макросы выбирают сотрудники, и постепенно поднимайте их рейтинг.
- **Фильтруйте по условиям**: сначала отсекайте несовместимые макросы (условия), затем выбирайте лучший по скору.

## 5. Метрики качества макроса

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
