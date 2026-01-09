# Перечень функций, сценариев и макросов

## Определения

- **Функция** — атомарная бизнес-операция системы, выполняемая через API/интерфейс и имеющая четко описанные входы и выходы (например, `create_task`, `assign_role`).
- **Сценарий** — последовательность действий пользователя/системы, объединяющая несколько функций для достижения конкретной цели (например, «создать проект и первую задачу»).
- **Макрос** — заранее заданная автоматизация (шаблон сценария), которая объединяет функции в повторяемый поток с минимальным участием пользователя.
- **Приложение** — внутренний модуль с UI или внешняя система/сервис, с которым предусмотрена интеграция (например, почтовый сервис, мессенджер, BI).

## Перечень 50 функций (сгруппировано по темам)

### Пользователи и доступ

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 1 | `create_user` | Создает пользователя в системе. | `email`, `phone`, `name`, `roles[]` | `user_id`, `created_at` |
| 2 | `update_user_profile` | Обновляет профиль пользователя. | `user_id`, `name`, `avatar_url`, `timezone` | `user_id`, `updated_at` |
| 3 | `deactivate_user` | Блокирует пользователя без удаления данных. | `user_id`, `reason` | `user_id`, `status` |
| 4 | `list_users` | Возвращает список пользователей с фильтрами. | `filters`, `page`, `page_size` | `items[]`, `total` |
| 5 | `get_user` | Получает подробную карточку пользователя. | `user_id` | `user` |
| 6 | `create_role` | Создает роль доступа. | `name`, `permissions[]` | `role_id` |
| 7 | `assign_role` | Назначает роль пользователю. | `user_id`, `role_id` | `user_id`, `role_id` |
| 8 | `list_roles` | Возвращает роли. | `filters` | `items[]` |
| 9 | `create_permission` | Создает разрешение. | `name`, `scope` | `permission_id` |
| 10 | `list_permissions` | Возвращает перечень разрешений. | `filters` | `items[]` |

### Команды

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 11 | `create_team` | Создает команду. | `name`, `owner_id` | `team_id` |
| 12 | `update_team` | Обновляет параметры команды. | `team_id`, `fields{}` | `team_id`, `updated_at` |
| 13 | `add_team_member` | Добавляет пользователя в команду. | `team_id`, `user_id`, `role` | `team_id`, `user_id` |
| 14 | `remove_team_member` | Удаляет пользователя из команды. | `team_id`, `user_id` | `team_id`, `user_id` |
| 15 | `list_team_members` | Возвращает участников команды. | `team_id`, `page` | `items[]`, `total` |

### Проекты

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 16 | `create_project` | Создает проект для команды. | `name`, `owner_id`, `tags[]` | `project_id`, `created_at` |
| 17 | `update_project` | Обновляет параметры проекта. | `project_id`, `name`, `status` | `project_id`, `updated_at` |
| 18 | `archive_project` | Архивирует проект без удаления. | `project_id`, `reason` | `project_id`, `archived_at` |
| 19 | `list_projects` | Возвращает список проектов. | `filters`, `page`, `page_size` | `items[]`, `total` |
| 20 | `get_project` | Возвращает карточку проекта. | `project_id` | `project` |

### Задачи

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 21 | `create_task` | Создает задачу в проекте. | `project_id`, `title`, `assignee_id`, `due_date` | `task_id`, `created_at` |
| 22 | `update_task` | Обновляет данные задачи. | `task_id`, `fields{}` | `task_id`, `updated_at` |
| 23 | `complete_task` | Отмечает задачу выполненной. | `task_id`, `completed_by` | `task_id`, `completed_at` |
| 24 | `reopen_task` | Возвращает задачу в работу. | `task_id`, `reason` | `task_id`, `status` |
| 25 | `list_tasks` | Возвращает задачи с фильтрами. | `project_id`, `filters`, `page` | `items[]`, `total` |
| 26 | `get_task` | Возвращает подробности задачи. | `task_id` | `task` |

### Комментарии и файлы

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 27 | `add_comment` | Добавляет комментарий к объекту. | `entity_type`, `entity_id`, `author_id`, `text` | `comment_id`, `created_at` |
| 28 | `list_comments` | Возвращает комментарии объекта. | `entity_type`, `entity_id`, `page` | `items[]`, `total` |
| 29 | `upload_file` | Загружает файл и сохраняет метаданные. | `file`, `owner_id`, `tags[]` | `file_id`, `url` |
| 30 | `get_file` | Возвращает метаданные файла. | `file_id` | `file` |
| 31 | `delete_file` | Удаляет файл с хранением истории. | `file_id`, `reason` | `file_id`, `status` |

### Теги

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 32 | `create_tag` | Создает тег для классификации. | `name`, `color` | `tag_id` |
| 33 | `list_tags` | Возвращает список тегов. | `filters` | `items[]` |
| 34 | `assign_tag` | Назначает тег объекту. | `entity_type`, `entity_id`, `tag_id` | `entity_id`, `tag_id` |
| 35 | `remove_tag` | Снимает тег с объекта. | `entity_type`, `entity_id`, `tag_id` | `entity_id`, `tag_id` |

### Уведомления и вебхуки

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 36 | `create_notification` | Создает уведомление пользователю. | `user_id`, `title`, `body`, `channel` | `notification_id` |
| 37 | `list_notifications` | Возвращает уведомления пользователя. | `user_id`, `status`, `page` | `items[]`, `total` |
| 38 | `mark_notification_read` | Помечает уведомление прочитанным. | `notification_id` | `notification_id`, `read_at` |
| 39 | `create_webhook` | Создает вебхук на событие. | `event`, `target_url`, `secret` | `webhook_id` |
| 40 | `list_webhooks` | Возвращает список вебхуков. | `filters` | `items[]` |
| 41 | `delete_webhook` | Удаляет вебхук. | `webhook_id` | `webhook_id`, `status` |

### Аудит и отчеты

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 42 | `create_audit_entry` | Записывает событие аудита. | `actor_id`, `action`, `entity` | `audit_id`, `created_at` |
| 43 | `list_audit_entries` | Возвращает аудит с фильтрами. | `filters`, `page` | `items[]`, `total` |
| 44 | `create_report` | Создает отчет по данным. | `name`, `query`, `schedule` | `report_id` |
| 45 | `run_report` | Запускает генерацию отчета. | `report_id`, `parameters{}` | `run_id`, `status` |
| 46 | `get_report_result` | Возвращает результат отчета. | `run_id` | `report_result` |

### Импорт/экспорт и мониторинг

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 47 | `export_data` | Экспортирует данные в файл. | `entity`, `filters`, `format` | `export_id`, `url` |
| 48 | `import_data` | Импортирует данные из файла. | `entity`, `file`, `mode` | `import_id`, `status` |
| 49 | `health_check` | Возвращает статус сервисов. | `scope` | `status`, `services[]` |
| 50 | `get_system_metrics` | Возвращает системные метрики. | `from`, `to`, `metrics[]` | `series[]` |

## 20 основных пользовательских сценариев

| № | Цель | Шаги | Ожидаемый результат |
| --- | --- | --- | --- |
| 1 | Онбординг нового пользователя | 1) Вызвать `create_user`. 2) Отправить приветственное уведомление через `create_notification`. | Пользователь создан, уведомление доставлено. |
| 2 | Назначение роли администратору | 1) Найти пользователя `get_user`. 2) Вызвать `assign_role`. | Пользователь получил права администратора. |
| 3 | Создание проекта и первой задачи | 1) `create_project`. 2) `create_task` с `assignee_id`. | Проект и задача зарегистрированы. |
| 4 | Обновление срока задачи | 1) `get_task`. 2) `update_task` с новым `due_date`. | Задача обновлена, дата изменена. |
| 5 | Завершение работы по задаче | 1) `complete_task`. 2) `add_comment` о результате. | Задача завершена и документирована. |
| 6 | Возобновление задачи | 1) `reopen_task` с причиной. | Статус задачи вернулся в работу. |
| 7 | Архивация проекта | 1) Проверить активные задачи через `list_tasks`. 2) `archive_project`. | Проект в архиве, активные задачи отсутствуют. |
| 8 | Подготовка отчета по проекту | 1) `create_report`. 2) `run_report`. 3) `get_report_result`. | Получен отчет и результат. |
| 9 | Экспорт данных для аналитики | 1) `export_data` с фильтрами. | Экспорт завершен, доступна ссылка на файл. |
| 10 | Импорт данных из внешней системы | 1) `import_data` в режиме `merge`. | Данные импортированы, статус успешный. |
| 11 | Создание команды и добавление участников | 1) `create_team`. 2) `add_team_member` для пользователей. | Команда создана, участники добавлены. |
| 12 | Обновление профиля пользователя | 1) `update_user_profile`. | Профиль обновлен. |
| 13 | Настройка вебхука на события задач | 1) `create_webhook` для события `task.updated`. | Вебхук активен и готов принимать события. |
| 14 | Очистка старых файлов | 1) `export_data` по сущности `file` с фильтром. 2) `delete_file`. | Файл удален, запись сохранена. |
| 15 | Назначение тегов проекту | 1) `create_tag` (если нет). 2) `assign_tag` для проекта. | Теги отображаются у проекта. |
| 16 | Снятие тега с задачи | 1) `remove_tag`. | Тег снят. |
| 17 | Просмотр уведомлений | 1) `list_notifications`. 2) `mark_notification_read`. | Уведомления помечены как прочитанные. |
| 18 | Просмотр аудита действий | 1) `list_audit_entries` по фильтру пользователя. | Список аудита получен. |
| 19 | Мониторинг здоровья системы | 1) `health_check`. | Получен статус всех сервисов. |
| 20 | Получение метрик за период | 1) `get_system_metrics` для `cpu`, `memory`. | Возвращены временные ряды метрик. |

## 10 макросов (шаблоны автоматизации)

| № | Название макроса | Описание | Шаги (связка функций) |
| --- | --- | --- | --- |
| 1 | `macro_onboard_user` | Полный онбординг пользователя. | `create_user` → `assign_role` → `create_notification` |
| 2 | `macro_project_kickoff` | Запуск проекта с базовой структурой. | `create_project` → `create_task` (шаблон) → `assign_tag` |
| 3 | `macro_task_completion` | Завершение задачи с протоколом. | `complete_task` → `add_comment` → `create_audit_entry` |
| 4 | `macro_archive_project` | Архивация проекта с проверкой. | `list_tasks` → `archive_project` → `create_audit_entry` |
| 5 | `macro_team_setup` | Быстрое создание команды. | `create_team` → `add_team_member` (циклом) → `create_notification` |
| 6 | `macro_webhook_setup` | Настройка вебхука по шаблону. | `create_webhook` → `create_audit_entry` |
| 7 | `macro_tag_cleanup` | Обновление тегов объектов. | `remove_tag` → `assign_tag` → `create_audit_entry` |
| 8 | `macro_report_delivery` | Генерация и доставка отчета. | `run_report` → `get_report_result` → `create_notification` |
| 9 | `macro_bulk_export` | Массовый экспорт данных. | `export_data` → `create_audit_entry` |
| 10 | `macro_incident_check` | Быстрая проверка инцидента. | `health_check` → `get_system_metrics` → `create_audit_entry` |

## Сверка объема с ресурсами и сроками

- **Объем**: 50 функций, 20 пользовательских сценариев, 10 макросов, 20 интеграций/приложений.
- **Ресурсы**: состав команды и доступность экспертов требуют фиксации в `integration_inventory.md`.
- **Сроки**: в `timeline.md` отсутствуют оценки длительности и дат; необходимо заполнить базовые оценки и буферы, чтобы подтвердить реализуемость объема.
- **Вывод**: текущий объем зафиксирован, но подтверждение сроков возможно только после заполнения оценок и ресурсов.

## Формат хранения и правила именования

### Формат хранения

* **Основной формат хранения**: JSON-документы.
* **Хранение табличных представлений**: реляционная БД (таблицы отражают JSON-поля).
* **Обмен между сервисами**: JSON по HTTP API.

Пример JSON-сущности `task`:

```json
{
  "task_id": "tsk_123",
  "project_id": "prj_001",
  "title": "Согласовать договор",
  "assignee_id": "usr_045",
  "status": "in_progress",
  "due_date": "2025-02-28",
  "tags": ["legal", "priority"],
  "created_at": "2025-02-10T12:00:00Z",
  "updated_at": "2025-02-11T09:00:00Z"
}
```

### Правила именования

* **Функции**: `snake_case` глагол + объект (`create_task`, `list_users`).
* **Сущности**: `snake_case` (`user`, `project`, `task`).
* **Идентификаторы**: префикс + уникальный идентификатор (`usr_`, `prj_`, `tsk_`).
* **Поля времени**: `*_at` в ISO 8601 UTC (`created_at`).
* **Списки**: суффикс `[]` в документации (`roles[]`, `items[]`).
* **Состояния**: `status` со значениями из enum (`active`, `inactive`, `archived`).
