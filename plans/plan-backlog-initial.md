# Первичный backlog по доменным областям

## Компоненты по доменам

| Доменная область | API | Хранение | Модерация | Рейтинги | Интеграции |
| --- | --- | --- | --- | --- | --- |
| Пользователи и доступ | Методы управления пользователями и ролями (`create_user`, `assign_role`, `list_roles`). | Таблицы `user`, `role`, `permission`. | N/A | N/A | SSO/IdP, внешние каталоги пользователей. |
| Команды | CRUD-команды (`create_team`, `add_team_member`). | `team`, `team_member`. | N/A | N/A | Корпоративные справочники команд. |
| Проекты | CRUD-проекты (`create_project`, `list_projects`). | `project`, `project_tag`. | N/A | N/A | Импорт проектов из внешних трекеров. |
| Задачи | CRUD-задачи (`create_task`, `complete_task`). | `task`, `task_status_history`. | N/A | N/A | Синхронизация с трекерами задач. |
| Комментарии и файлы | `add_comment`, `upload_file`, `delete_file`. | `comment`, `file`, `file_version`. | N/A | N/A | Хранилища файлов, CDN. |
| Теги | `create_tag`, `assign_tag`. | `tag`, `tag_assignment`. | N/A | N/A | Импорт классификаторов. |
| Уведомления и вебхуки | `create_notification`, `create_webhook`. | `notification`, `webhook`. | N/A | N/A | Email/SMS/Push провайдеры. |
| Аудит и отчеты | `create_audit_entry`, `create_report`. | `audit_log`, `report`, `report_run`. | N/A | N/A | BI/аналитические платформы. |
| Импорт/экспорт и мониторинг | `export_data`, `import_data`, `health_check`. | `export_job`, `import_job`, `service_status`. | N/A | N/A | S3/Blob, системы мониторинга. |
| Отзывы и подтверждения | `create_review`, `create_verified_usage`, `list_reviews`. | `review`, `verified_usage`. | Очередь проверок верификации (если нужно). | `rating` как часть отзывов. | Источники подтверждений использования. |
| Модерация отзывов | `enqueue_review_moderation`, `moderate_review`, `list_moderation_queue`. | `moderation_queue`, `moderation_decision`, `fraud_signal`. | Логи решений, антифрод сигналы. | Влияние на итоговый рейтинг. | Инструменты модерации/антифрод провайдеры. |
| Рейтинги | `recalculate_ratings`, `get_rating` (планируется). | `rating`, `rating_history`. | N/A | Пересчет и хранение агрегатов. | Экспорт рейтингов в витрины. |
| Аналитика, рост, поддержка | `track_funnel`, `calculate_ltv`, `create_support_ticket`. | `funnel_event`, `segment_metric`, `support_ticket`. | N/A | N/A | CRM/Support/Marketing платформы. |

## Первичный backlog

| ID | Домен | Задача | Описание | Приоритет | Владелец | Этап Roadmap | Этап Timeline |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BL-001 | Пользователи и доступ | Спецификация API управления пользователями | Контракты методов `create_user`, `update_user_profile`, `deactivate_user`, `list_users`, `get_user`. | P0 | Product Owner + Backend Lead | Discovery | 1. Discovery & scope |
| BL-002 | Пользователи и доступ | Модель хранения пользователей/ролей | Таблицы `user`, `role`, `permission`, связи для назначения ролей. | P0 | Backend Lead | Design | 2. Requirements & solution design |
| BL-003 | Команды | CRUD и членство команд | API `create_team`, `update_team`, `add_team_member`, `remove_team_member`. | P1 | Backend Engineer | Development | 3. Implementation |
| BL-004 | Проекты | API проекта и статусы | Контракты `create_project`, `update_project`, `archive_project`, фильтры `list_projects`. | P1 | Product Owner + Backend Lead | Design | 2. Requirements & solution design |
| BL-005 | Задачи | Модель задач и статусов | Хранилище `task`, история статусов, валидации `complete_task`/`reopen_task`. | P1 | Backend Lead | Design | 2. Requirements & solution design |
| BL-006 | Комментарии и файлы | Поток загрузки и удаления файлов | API `upload_file`, `get_file`, `delete_file`, политика хранения. | P1 | Backend Engineer | Development | 3. Implementation |
| BL-007 | Теги | Классификация сущностей | Таблицы `tag`, `tag_assignment`, API `create_tag`, `assign_tag`. | P2 | Backend Engineer | Development | 3. Implementation |
| BL-008 | Уведомления и вебхуки | Каналы уведомлений и вебхуки | Описание интеграций и событий для `create_notification`, `create_webhook`. | P1 | Backend Engineer | Design | 2. Requirements & solution design |
| BL-009 | Аудит и отчеты | Аудит логов | Формат `create_audit_entry`, хранение `audit_log`. | P0 | Backend Lead | Design | 2. Requirements & solution design |
| BL-010 | Импорт/экспорт | Пайплайн импорт/экспорт | Спецификации `import_data`, `export_data`, форматы и статусы. | P1 | Backend Engineer | Development | 3. Implementation |
| BL-011 | Мониторинг | Метрики и health-check | Контракты `health_check`, `get_system_metrics`, алерты. | P1 | SRE/DevOps | Development | 3. Implementation |
| BL-012 | Отзывы и подтверждения | Проверка `verified_usage` | Правила валидации `create_review` через `create_verified_usage`. | P0 | Product Owner + Backend Lead | Design | 2. Requirements & solution design |
| BL-013 | Отзывы и подтверждения | Хранилище отзывов | Схемы `review`, `verified_usage` и связи с сущностями. | P0 | Backend Lead | Design | 2. Requirements & solution design |
| BL-014 | Модерация | Очередь модерации отзывов | Реализация `enqueue_review_moderation`, `list_moderation_queue`, статусная модель. | P0 | Automation Lead | Development | 3. Implementation |
| BL-015 | Модерация | Решения модерации и аудит | `moderate_review`, `log_moderation_decision`, журнал решений. | P0 | Automation Lead | Development | 3. Implementation |
| BL-016 | Антифрод | Расчет fraud-score | `detect_review_fraud`, таблица `fraud_signal`, метрики. | P1 | Automation Lead | Development | 3. Implementation |
| BL-017 | Рейтинги | Пересчет рейтингов | `recalculate_ratings`, хранение агрегатов и истории. | P0 | Backend Lead | Development | 3. Implementation |
| BL-018 | Интеграции | Каналы внешних данных | Определить источники отзывов/подтверждений, протоколы импорта. | P1 | Product Owner + Catalog Lead | Discovery | 1. Discovery & scope |
| BL-019 | QA | Набор тестовых сценариев | Тест-план для основных сценариев и модерации. | P1 | QA Lead | QA | 4. QA & validation |
| BL-020 | Release | Подготовка релизного пакета | Релиз-ноты, чеклист и мониторинг. | P2 | Release Manager | Release | 5. Release & handover |

## Связь с Roadmap и Timeline

- Этапы Roadmap соответствуют стадиям `plan-roadmap.md`: Discovery, Design, Development, QA, Release.
- Этапы Timeline отражают табличные стадии `plan-timeline.md` (1–5) и используются для планирования дат.
