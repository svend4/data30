# Макросы: примеры и рекомендации

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
