# Инвентаризация интеграций и экспертов

## 1) Внешние системы/поставщики

| Система/поставщик | Назначение/контекст | Контактное лицо (имя/роль) | Канал связи | SLA/ограничения | Комментарии |
| --- | --- | --- | --- | --- | --- |
| SendGrid (email) | Отправка системных писем и уведомлений. | Мария Крылова (email deliverability manager) | sendgrid-support@company.example | Поддержка 24/7, лимит 100k писем/сутки, SLA 99.9%. | SMTP/API. |
| Twilio (SMS) | Отправка SMS и двухфакторной аутентификации. | Илья Романов (telecom integrations lead) | twilio@company.example | 24/7, лимит 10 SMS/сек, зависимость от региональных операторов. | SMS/Verify API. |
| Firebase Cloud Messaging | Push-уведомления мобильным клиентам. | Екатерина Мостовая (mobile platform owner) | mobile-platform@company.example | Best-effort доставка, ограничения по токенам/региону, SLA отсутствует. | FCM токены. |
| Okta SSO | SSO для корпоративных пользователей. | Сергей Мельников (IAM owner) | iam@company.example | SLA 99.9%, плановые окна 02:00-04:00 UTC. | SAML/OIDC. |
| Azure AD | Каталог пользователей и групп. | Олег Сафонов (directory services lead) | azuread@company.example | SLA 99.9%, лимиты Graph API 10k запросов/10 мин. | SCIM/Graph API. |
| Google Calendar | Планирование задач и напоминания. | Анна Ясная (workplace apps owner) | workspace-apps@company.example | SLA 99.9%, лимиты API 1M запросов/день. | OAuth2. |
| Microsoft 365 Calendar | Планирование встреч и напоминаний. | Дмитрий Ковалев (M365 integrations lead) | m365@company.example | SLA 99.9%, лимиты Graph API 10k запросов/10 мин. | Graph API. |
| Amazon S3 | Хранилище файлов и экспортов. | Наталья Лукина (storage owner) | storage@company.example | SLA 99.9%, лимит 3.5k PUT/сек/префикс. | Объектное хранилище. |
| Google Drive | Обмен отчетами и файлами. | Анна Ясная (workplace apps owner) | workspace-apps@company.example | SLA 99.9%, лимит 1B запросов/день. | OAuth2. |
| SharePoint | Внутренний документооборот. | Дмитрий Ковалев (M365 integrations lead) | m365@company.example | SLA 99.9%, лимиты Graph API 10k запросов/10 мин. | Graph API. |
| Slack | Уведомления и боты. | Виктория Орлова (collaboration tools owner) | collab-tools@company.example | SLA 99.9%, лимит 1 сообщение/сек на приложение. | Webhooks/Apps. |
| Microsoft Teams | Уведомления в рабочих каналах. | Виктория Орлова (collaboration tools owner) | collab-tools@company.example | SLA 99.9%, лимит 4 сообщения/сек на приложение. | Webhooks/Apps. |
| Zoom | Онлайн-встречи по задачам/проектам. | Алексей Титов (video conferencing owner) | zoom@company.example | SLA 99.9%, лимит API 100 запросов/сек. | OAuth2/API. |
| Power BI | Аналитические дашборды. | Ирина Забелина (BI owner) | bi@company.example | SLA 99.9%, обновление датасетов до 8 раз/сутки. | Dataset refresh. |
| Amplitude | Продуктовая аналитика. | Павел Лисов (product analytics lead) | product-analytics@company.example | SLA 99.9%, лимит 10M событий/день. | Event tracking. |
| Datadog | Мониторинг инфраструктуры и метрик. | Кирилл Белов (SRE monitoring lead) | sre-monitoring@company.example | SLA 99.9%, лимит 200 метрик/хост. | Metrics/Logs. |
| Sentry | Трекинг ошибок и алерты. | Юлия Гребнева (app reliability lead) | app-reliability@company.example | SLA 99.9%, лимит 50k событий/час. | Error events. |
| Jira | Управление задачами и инцидентами. | Андрей Ким (delivery tools owner) | jira-admins@company.example | SLA 99.9%, лимит API 100 запросов/10 сек. | REST API. |
| Salesforce | Интеграция с CRM. | Марина Шестакова (CRM owner) | crm@company.example | SLA 99.9%, лимит 15k запросов/сутки, batch до 10k записей. | REST/Bulk API. |
| Zapier/Make | Низкодовые автоматизации. | Никита Зорин (automation lead) | automation@company.example | Best-effort, лимиты 100 задач/15 мин. | Webhooks/Triggers. |

## 2) Внутренние команды/сервисы и интеграции

| Команда/сервис | Владелец | Интерфейс (API/протокол) | Точки интеграции | Зависимости/ограничения | Комментарии |
| --- | --- | --- | --- | --- | --- |
| Core Platform API | Елена Новикова (platform owner) | REST/gRPC | Авторизация, профили пользователей, ключи API. | Версия API v2, обязательная OAuth2, лимит 500 RPS. | Критический путь для всех внешних интеграций. |
| Data Warehouse | Константин Борисов (data platform lead) | SQL/ETL (Airflow) | Выгрузка событий, аналитические витрины. | Окно ETL 01:00-03:00 UTC, задержка до 2 часов. | Требует согласования схем. |
| Notification Service | Мария Крылова (messaging lead) | REST/AMQP | Email/SMS/Push маршрутизация. | SLA 99.95%, retry policy 3 попытки, лимит 5k сообщений/мин. | Использует SendGrid/Twilio/FCM. |
| Identity Service | Сергей Мельников (IAM owner) | OIDC/SAML/SCIM | SSO, управление ролями. | Изменения схем ролей через CAB, SLA 99.9%. | Интеграция с Okta/Azure AD. |
| Billing & Subscriptions | Полина Юрьева (billing owner) | REST/Webhooks | Статус подписок, биллинг событий. | Обновление каждые 15 мин, Webhook retry 24 часа. | Требует PCI-сегмента. |
| Observability Stack | Кирилл Белов (SRE monitoring lead) | Prometheus/Datadog API | Метрики, алерты, трассировка. | 99.9%, retention 30 дней. | Совместно с SRE. |

## 3) Доступность экспертов

| Эксперт | Роль/область | Окна доступности | Замены/бэкапы | Контактный канал | Комментарии |
| --- | --- | --- | --- | --- | --- |
| Мария Крылова | Messaging/Deliverability | Пн-Пт 10:00-18:00 MSK | Виктор Синицын | sendgrid-support@company.example | Экстренные инциденты через on-call. |
| Сергей Мельников | IAM/SSO | Пн-Пт 09:00-17:00 MSK | Олег Сафонов | iam@company.example | CAB по средам 14:00 MSK. |
| Кирилл Белов | SRE/Monitoring | 24/7 on-call | Дарья Федорова | sre-monitoring@company.example | Эскалация через PagerDuty. |
| Анна Ясная | Workplace apps | Пн-Пт 10:00-19:00 MSK | Дмитрий Ковалев | workspace-apps@company.example | Основной контакт по календарям/диску. |
| Павел Лисов | Product analytics | Пн-Пт 11:00-20:00 MSK | Ирина Забелина | product-analytics@company.example | Поддержка трекинга событий. |
| Елена Новикова | Core platform | Пн-Пт 09:00-18:00 MSK | Константин Борисов | platform@company.example | Любые изменения API через RFC. |

## 4) Проверка полноты и утверждение

- [x] Провести рабочую сессию по полноте списка (дата/время: 2026-01-09 11:00 MSK, участники: продукт, платформа, SRE, безопасность).
- [x] Зафиксировать решения/правки по итогам сессии.
- [x] Утвердить у владельцев (перечень владельцев: руководитель продукта, руководитель платформы, SRE lead, дата: 2026-01-09).
- [x] Опубликовать финальную версию и уведомить заинтересованных.
