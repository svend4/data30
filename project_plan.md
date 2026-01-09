# План работ и организационная структура проекта

## 1. Этапы / области работ
1. Discovery
2. Design
3. Development
4. QA
5. Release

## 2. Оценки длительности по этапам и ключевым задачам
> Формат: этап / задача — оценка длительности — ответственный владелец

### Discovery (1–2 недели)
- Анализ требований и целей — 3–5 дней — Product Manager
- Сбор и приоритизация стейкхолдеров — 2–3 дня — Product Manager
- Формирование product backlog и roadmap — 2–4 дня — Product Manager

### Design (2–3 недели)
- Архитектурное проектирование — 5–7 дней — Solution Architect
- UX/UI прототипирование — 5–8 дней — UX/UI Designer
- Проработка нефункциональных требований — 3–5 дней — Tech Lead

### Development (4–8 недель)
- Настройка инфраструктуры/репозитория — 2–4 дня — DevOps Engineer
- Реализация ключевых фич (MVP) — 15–25 дней — Engineering Team
- Интеграции и API — 10–15 дней — Backend Engineer

### QA (2–3 недели)
- Подготовка тест-плана и сценариев — 3–5 дней — QA Lead
- Функциональное тестирование — 7–10 дней — QA Team
- Регрессионное тестирование — 3–5 дней — QA Team

### Release (1–2 недели)
- Подготовка релиза (релиз-ноты, чеклисты) — 2–3 дня — Release Manager
- Деплой на прод — 1–2 дня — DevOps Engineer
- Пострелизный мониторинг — 3–5 дней — SRE/DevOps

## 3. WBS (Phase → Workstream → Tasks → Deliverables)
| Phase | Workstream | Tasks | Deliverables | MVP/Beta/Scale | Responsible (RACI-compatible role) |
| --- | --- | --- | --- | --- | --- |
| Discovery | Product discovery | Анализ требований и целей, сбор стейкхолдеров, формирование backlog/roadmap | Подтвержденные требования, приоритизированный backlog | MVP | Product Manager |
| Design | UX/UI | Прототипирование ключевых экранов (вход, каталог, рекомендация, подтверждение), согласование навигации | Прототип с 4 экранами и лог навигации | MVP | UX/UI Designer |
| Design | Architecture | Архитектурное проектирование, проработка NFR, базовая схема данных | Архитектура решения, NFR-спецификация | MVP | Solution Architect |
| Development | Core CRUD | Реализация базовых сценариев для `user/project/task`: create/list/get/update, базовый статус задач | Работающие CRUD сценарии, API/логика | MVP | Backend Engineer |
| Development | UX flow | Реализация UX-минимума: вход → каталог → рекомендация → подтверждение | End-to-end UX-флоу MVP | MVP | Frontend Engineer |
| Development | Notifications | Уведомления пользователям (create/list/mark read) | Базовые уведомления в продукте | Beta | Backend Engineer |
| Development | Automation | Макросы для онбординга, старта проекта, завершения задач | Базовые макросы автоматизации | Beta | Backend Engineer |
| Development | Integrations | Вебхуки событий, отчеты и экспорт данных | Интеграции и отчеты для расширенных сценариев | Beta | Backend Engineer |
| Development | Observability | Реализация health-check и системных метрик (`health_check`, `get_system_metrics`) | Доступные health-check и метрики | Scale | Backend Engineer |
| QA | Functional QA | Подготовка тест-плана, сценарии по core CRUD и UX флоу MVP | Протоколы функционального тестирования | MVP | QA Lead / QA Engineer |
| QA | Regression/Automation | Регрессия по расширенным сценариям, проверка макросов/уведомлений/вебхуков/отчетов | Регрессионный набор Beta | Beta | QA Lead / QA Engineer |
| QA | Reliability | Нагрузочные тесты, регрессия, проверка health-check/метрик | Отчет о стабильности и метриках | Scale | QA Lead / QA Engineer |
| Release | Release prep | Релиз-ноты, чеклисты, подготовка окружений | Release package | MVP/Beta | Release Manager |
| Release | Operations | Деплой, мониторинг, сбор метрик/health-check, пострелизный мониторинг | Production release + post-release monitoring | Scale | DevOps Engineer / SRE |

## 4. Реестр рисков
| Риск | Вероятность | Влияние | Меры реагирования |
| --- | --- | --- | --- |
| Неопределенность требований на старте | Средняя | Высокое | Формализовать требования, проводить регулярные демо и согласования |
| Задержки интеграций со сторонними системами | Средняя | Среднее | Раннее согласование API, буфер по срокам |
| Недостаток ресурсов/людей | Средняя | Высокое | Резервный план, привлечение внешних подрядчиков |
| Регрессии при частых релизах | Высокая | Среднее | Автоматизация тестов, регрессионный набор |
| Низкая производительность/масштабируемость | Низкая | Высокое | Нагрузочное тестирование и профилирование |

## 5. Состав команды / ролей (для назначения R/A по RACI)
- Product Manager
- Solution Architect
- Tech Lead
- UX/UI Designer
- Backend Engineer
- Frontend Engineer
- QA Lead / QA Engineer
- DevOps Engineer / SRE
- Release Manager

## 6. Зависимости между этапами
- Discovery блокирует старт Design.
- Design блокирует Development (архитектура и UX/UI).
- Development блокирует QA (доступность фич).
- QA блокирует Release (подтверждение качества).
- Release зависит от готовности DevOps/инфраструктуры.
