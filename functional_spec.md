# Перечень функций, сценариев и макросов

## Термины и определения

- **Функция** — атомарная операция (API-метод или сервисная команда), выполняющая одно действие над сущностью и имеющая четко описанные входы/выходы.
- **Сценарий** — последовательность функций, объединенная общей пользовательской целью и ожидаемым результатом.
- **Макрос** — автоматизированный сценарий с явным триггером, условиями, шагами и политикой обработки ошибок.
- **Приложение** — внешняя или внутренняя система/продукт из каталога, с которым возможна интеграция и который предоставляет набор функций в домене.

## Таблица объёма

| Сущность | Целевой объём | Источник перечня |
| --- | --- | --- |
| Функции | 50 | См. раздел «Перечень 50 функций» |
| Сценарии | 20 | См. раздел «20 типовых сценариев использования» |
| Макросы | 10 | См. раздел «10 макросов (шаблоны автоматизации)» |
| Приложения | 20 | См. раздел «20 приложений каталога (MVP)» |

## Критерии приёма (минимальный набор возможностей)

### Функция
- Описаны входы, выходы и ошибки.
- Есть проверка прав доступа и валидация входных данных.
- Предусмотрена идемпотентность или явно указанно её отсутствие.
- Добавлена запись в аудит при изменении данных.

### Сценарий
- Сформулирована цель и ожидаемый результат.
- Перечислены шаги с использованием функций.
- Указаны предусловия и критерии успешного завершения.

### Макрос
- Определен триггер запуска.
- Описаны шаги и порядок выполнения.
- Есть условия выполнения и политика обработки ошибок.
- Определен результат (выходные артефакты/статус).

### Приложение
- Имеется карточка в каталоге (id, имя, платформы, функции, совместимость).
- Указан статус поддержки и зрелость.
- Определены базовые сценарии использования и модель лицензирования.

## Владельцы групп сущностей

| Группа сущностей | Владелец (роль) | Зона ответственности |
| --- | --- | --- |
| Функции | Product Owner + Backend Lead | Контракты API, корректность входов/выходов, аудит. |
| Сценарии | Product Owner + Business Analyst | Бизнес-цели, шаги, критерии успеха. |
| Макросы | Automation Lead | Триггеры, шаги, обработка ошибок, мониторинг. |
| Приложения | Catalog Lead | Полнота карточек, совместимость, зрелость и лицензии. |

## Перечень 50 функций

| № | Название функции | Описание | Входы | Выходы |
| --- | --- | --- | --- | --- |
| 1 | `create_user` | Создает пользователя в системе. | `email`, `phone`, `name`, `roles[]` | `user_id`, `created_at` |
| 2 | `update_user_profile` | Обновляет профиль пользователя. | `user_id`, `name`, `avatar_url`, `timezone` | `user_id`, `updated_at` |
| 3 | `deactivate_user` | Блокирует пользователя без удаления данных. | `user_id`, `reason` | `user_id`, `status` |
| 4 | `list_users` | Возвращает список пользователей с фильтрами. | `filters`, `page`, `page_size` | `items[]`, `total` |
| 5 | `get_user` | Получает подробную карточку пользователя. | `user_id` | `user` |
| 6 | `create_project` | Создает проект для команды. | `name`, `owner_id`, `tags[]` | `project_id`, `created_at` |
| 7 | `update_project` | Обновляет параметры проекта. | `project_id`, `name`, `status` | `project_id`, `updated_at` |
| 8 | `archive_project` | Архивирует проект без удаления. | `project_id`, `reason` | `project_id`, `archived_at` |
| 9 | `list_projects` | Возвращает список проектов. | `filters`, `page`, `page_size` | `items[]`, `total` |
| 10 | `get_project` | Возвращает карточку проекта. | `project_id` | `project` |
| 11 | `create_task` | Создает задачу в проекте. | `project_id`, `title`, `assignee_id`, `due_date` | `task_id`, `created_at` |
| 12 | `update_task` | Обновляет данные задачи. | `task_id`, `fields{}` | `task_id`, `updated_at` |
| 13 | `complete_task` | Отмечает задачу выполненной. | `task_id`, `completed_by` | `task_id`, `completed_at` |
| 14 | `reopen_task` | Возвращает задачу в работу. | `task_id`, `reason` | `task_id`, `status` |
| 15 | `list_tasks` | Возвращает задачи с фильтрами. | `project_id`, `filters`, `page` | `items[]`, `total` |
| 16 | `get_task` | Возвращает подробности задачи. | `task_id` | `task` |
| 17 | `add_comment` | Добавляет комментарий к объекту. | `entity_type`, `entity_id`, `author_id`, `text` | `comment_id`, `created_at` |
| 18 | `list_comments` | Возвращает комментарии объекта. | `entity_type`, `entity_id`, `page` | `items[]`, `total` |
| 19 | `upload_file` | Загружает файл и сохраняет метаданные. | `file`, `owner_id`, `tags[]` | `file_id`, `url` |
| 20 | `get_file` | Возвращает метаданные файла. | `file_id` | `file` |
| 21 | `delete_file` | Удаляет файл с хранением истории. | `file_id`, `reason` | `file_id`, `status` |
| 22 | `create_tag` | Создает тег для классификации. | `name`, `color` | `tag_id` |
| 23 | `list_tags` | Возвращает список тегов. | `filters` | `items[]` |
| 24 | `assign_tag` | Назначает тег объекту. | `entity_type`, `entity_id`, `tag_id` | `entity_id`, `tag_id` |
| 25 | `remove_tag` | Снимает тег с объекта. | `entity_type`, `entity_id`, `tag_id` | `entity_id`, `tag_id` |
| 26 | `create_notification` | Создает уведомление пользователю. | `user_id`, `title`, `body`, `channel` | `notification_id` |
| 27 | `list_notifications` | Возвращает уведомления пользователя. | `user_id`, `status`, `page` | `items[]`, `total` |
| 28 | `mark_notification_read` | Помечает уведомление прочитанным. | `notification_id` | `notification_id`, `read_at` |
| 29 | `create_webhook` | Создает вебхук на событие. | `event`, `target_url`, `secret` | `webhook_id` |
| 30 | `list_webhooks` | Возвращает список вебхуков. | `filters` | `items[]` |
| 31 | `delete_webhook` | Удаляет вебхук. | `webhook_id` | `webhook_id`, `status` |
| 32 | `create_audit_entry` | Записывает событие аудита. | `actor_id`, `action`, `entity` | `audit_id`, `created_at` |
| 33 | `list_audit_entries` | Возвращает аудит с фильтрами. | `filters`, `page` | `items[]`, `total` |
| 34 | `create_team` | Создает команду. | `name`, `owner_id` | `team_id` |
| 35 | `update_team` | Обновляет параметры команды. | `team_id`, `fields{}` | `team_id`, `updated_at` |
| 36 | `add_team_member` | Добавляет пользователя в команду. | `team_id`, `user_id`, `role` | `team_id`, `user_id` |
| 37 | `remove_team_member` | Удаляет пользователя из команды. | `team_id`, `user_id` | `team_id`, `user_id` |
| 38 | `list_team_members` | Возвращает участников команды. | `team_id`, `page` | `items[]`, `total` |
| 39 | `create_role` | Создает роль доступа. | `name`, `permissions[]` | `role_id` |
| 40 | `assign_role` | Назначает роль пользователю. | `user_id`, `role_id` | `user_id`, `role_id` |
| 41 | `list_roles` | Возвращает роли. | `filters` | `items[]` |
| 42 | `create_permission` | Создает разрешение. | `name`, `scope` | `permission_id` |
| 43 | `list_permissions` | Возвращает перечень разрешений. | `filters` | `items[]` |
| 44 | `create_report` | Создает отчет по данным. | `name`, `query`, `schedule` | `report_id` |
| 45 | `run_report` | Запускает генерацию отчета. | `report_id`, `parameters{}` | `run_id`, `status` |
| 46 | `get_report_result` | Возвращает результат отчета. | `run_id` | `report_result` |
| 47 | `export_data` | Экспортирует данные в файл. | `entity`, `filters`, `format` | `export_id`, `url` |
| 48 | `import_data` | Импортирует данные из файла. | `entity`, `file`, `mode` | `import_id`, `status` |
| 49 | `health_check` | Возвращает статус сервисов. | `scope` | `status`, `services[]` |
| 50 | `get_system_metrics` | Возвращает системные метрики. | `from`, `to`, `metrics[]` | `series[]` |

## 20 типовых сценариев использования

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

## 20 приложений каталога (MVP)

| № | Приложение | Идентификатор каталога |
| --- | --- | --- |
| 1 | Slack | `slack` |
| 2 | Microsoft Teams | `microsoft-teams` |
| 3 | Zoom | `zoom` |
| 4 | Google Meet | `google-meet` |
| 5 | Jira Software | `jira` |
| 6 | Trello | `trello` |
| 7 | Asana | `asana` |
| 8 | Notion | `notion` |
| 9 | Confluence | `confluence` |
| 10 | GitHub | `github` |
| 11 | GitLab | `gitlab` |
| 12 | Bitbucket | `bitbucket` |
| 13 | Figma | `figma` |
| 14 | Miro | `miro` |
| 15 | Salesforce | `salesforce` |
| 16 | HubSpot | `hubspot` |
| 17 | Zendesk | `zendesk` |
| 18 | Intercom | `intercom` |
| 19 | Stripe | `stripe` |
| 20 | Shopify | `shopify` |

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
