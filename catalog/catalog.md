# Каталог приложений

## Назначение каталога

Каталог приложений описывает целевые инструменты, их ключевые функции, совместимость и условия использования. Он нужен для быстрого выбора решений под сценарии команды и для сопоставления приложений с функциональными потребностями проекта.

Каталог выступает минимальным справочником: карточки не стремятся заменить официальную документацию, но фиксируют критические данные (платформы, ограничения, зрелость, обновляемость), чтобы принимать продуктовые и интеграционные решения.

## Поля карточки приложения

Карточка приложения включает следующие поля:

- **Название** — человекочитаемое имя приложения.
- **Платформа** — поддерживаемые платформы (web, ios, android, desktop, cli, api).
- **Функции** — ключевые возможности (3–7 пунктов).
- **Ограничения** — важные условия/лимиты использования.
- **Цена** — ориентир стоимости/тарифа.
- **Зрелость** — стадия зрелости продукта (beta, stable, enterprise).
- **Совместимость** — проверенные интеграции с другими приложениями.
- **Документация** — ссылка на официальный центр помощи или документацию.

## Шаблон карточки приложения

| Поле | Описание | Пример |
| --- | --- | --- |
| `id` | Уникальный идентификатор (slug) | `slack` |
| `name` | Название приложения | `Slack` |
| `platforms` | Поддерживаемые платформы | `web, ios, android, desktop` |
| `functions` | Ключевые функции | `Командные чаты; Интеграции` |
| `limitations` | Ограничения/лимиты | `Лимит истории сообщений` |
| `price` | Ориентир цены | `freemium` |
| `compatibility` | Совместимые приложения | `jira, github` |
| `documentation` | Ссылка на документацию | `https://slack.com/help` |
| `support_status` | Статус поддержки | `active` |
| `maturity` | Зрелость | `enterprise` |
| `update_status` | Обновляемость | `active` |
| `use_cases` | Основные сценарии | `Командная коммуникация` |
| `licensing` | Модель лицензирования и стоимость | `subscription / tiered` |

## MVP-каталог (20–50 приложений)

| Приложение | Платформы | Цена | Зрелость | Обновляемость | Документация |
| --- | --- | --- | --- | --- | --- |
| Slack | web, ios, android, desktop | tiered | enterprise | active | https://slack.com/help |
| Microsoft Teams | web, ios, android, desktop | tiered | enterprise | active | https://learn.microsoft.com/microsoftteams/ |
| Zoom | web, ios, android, desktop | tiered | stable | active | https://support.zoom.com/ |
| Google Meet | web, ios, android | tiered | stable | active | https://support.google.com/meet/ |
| Jira Software | web | tiered | enterprise | active | https://support.atlassian.com/jira-software-cloud/ |
| Trello | web, ios, android | freemium | stable | active | https://support.atlassian.com/trello/ |
| Asana | web, ios, android | tiered | stable | active | https://asana.com/guide |
| Notion | web, ios, android, desktop | freemium | stable | active | https://www.notion.so/help |
| Confluence | web | tiered | enterprise | active | https://support.atlassian.com/confluence/ |
| GitHub | web, desktop, cli, api | freemium | enterprise | active | https://docs.github.com/ |
| GitLab | web, cli, api | tiered | enterprise | active | https://docs.gitlab.com/ |
| Bitbucket | web | tiered | stable | active | https://support.atlassian.com/bitbucket-cloud/ |
| Figma | web, desktop | tiered | enterprise | active | https://help.figma.com/ |
| Miro | web, ios, android, desktop | freemium | stable | active | https://help.miro.com/ |
| Salesforce | web, ios, android | tiered | enterprise | active | https://help.salesforce.com/ |
| HubSpot | web, ios, android | freemium | stable | active | https://knowledge.hubspot.com/ |
| Zendesk | web, ios, android | tiered | enterprise | active | https://support.zendesk.com/ |
| Intercom | web, ios, android | tiered | stable | active | https://www.intercom.com/help |
| Stripe | web, api | paid | enterprise | active | https://stripe.com/docs |
| Shopify | web, ios, android | tiered | enterprise | active | https://help.shopify.com/ |
| Mailchimp | web | freemium | stable | active | https://mailchimp.com/help/ |
| Google Drive | web, ios, android, desktop | tiered | stable | active | https://support.google.com/drive/ |
| Gmail | web, ios, android | freemium | stable | active | https://support.google.com/mail/ |
| Google Calendar | web, ios, android | freemium | stable | active | https://support.google.com/calendar/ |
| Microsoft Outlook | web, ios, android, desktop | tiered | enterprise | active | https://support.microsoft.com/outlook |
| SharePoint | web | tiered | enterprise | active | https://support.microsoft.com/sharepoint |
| Kubernetes | api, cli | free | enterprise | active | https://kubernetes.io/docs/ |
| Google Analytics | web | freemium | stable | active | https://support.google.com/analytics/ |

## Таблица «Приложение → Функции»

| Приложение | Функции |
| --- | --- |
| Slack | Командные чаты и каналы; Поиск по сообщениям и файлам; Интеграции с инструментами разработки; Автоматизация через workflow builder |
| Microsoft Teams | Чаты и видеозвонки; Совместная работа с файлами; Корпоративное управление доступом |
| Zoom | Видеоконференции; Вебинары; Запись встреч |
| Google Meet | Видеозвонки в браузере; Совместные встречи из календаря; Запись и транскрипция |
| Jira Software | Планирование спринтов; Управление бэклогом; Отчеты по задачам |
| Trello | Канбан-доски; Шаблоны проектов; Автоматизация Butler |
| Asana | Управление задачами; Таймлайны проектов; Шаблоны рабочих процессов |
| Notion | Документы и базы знаний; Таблицы и базы данных; Шаблоны рабочих пространств |
| Confluence | Документация команд; Совместное редактирование; Шаблоны страниц |
| GitHub | Хостинг репозиториев; Code review; CI/CD через GitHub Actions |
| GitLab | Репозитории и MR; CI/CD pipelines; Управление уязвимостями |
| Bitbucket | Git-репозитории; Pull requests; CI/CD через Pipelines |
| Figma | UI/UX дизайн; Совместное редактирование; Компонентные библиотеки |
| Miro | Онлайн-доски; Шаблоны воркшопов; Совместное рисование |
| Salesforce | CRM для продаж; Управление лидами; Отчеты и аналитика |
| HubSpot | CRM и маркетинговые кампании; Автоматизация писем; Воронки продаж |
| Zendesk | Тикетинг поддержки; База знаний; Омниканальные каналы |
| Intercom | Чат с клиентами; Автоматизация поддержки; Боты и help center |
| Stripe | Онлайн-платежи; Подписки и инвойсы; Управление рисками |
| Shopify | Интернет-магазин; Управление каталогом; Встроенные платежи |
| Mailchimp | Email-рассылки; Сегментация аудитории; Автоматизация маркетинга |
| Google Drive | Хранение файлов; Совместный доступ; Управление версиями |
| Gmail | Электронная почта; Интеграция с календарем; Фильтры и ярлыки |
| Google Calendar | Планирование встреч; Напоминания; Общие календари |
| Microsoft Outlook | Электронная почта; Календарь и контакты; Управление задачами |
| SharePoint | Корпоративные порталы; Совместные сайты; Управление документами |
| Kubernetes | Оркестрация контейнеров; Автоматическое масштабирование; Самовосстановление сервисов |
| Google Analytics | Аналитика трафика; Сегментация аудитории; Отчеты и дашборды |

## Таблица «Функция → Приложения»

| Функция | Приложения |
| --- | --- |
| CI/CD pipelines | GitLab |
| CI/CD через GitHub Actions | GitHub |
| CI/CD через Pipelines | Bitbucket |
| CRM для продаж | Salesforce |
| CRM и маркетинговые кампании | HubSpot |
| Code review | GitHub |
| Email-рассылки | Mailchimp |
| Git-репозитории | Bitbucket |
| Pull requests | Bitbucket |
| UI/UX дизайн | Figma |
| Автоматизация Butler | Trello |
| Автоматизация маркетинга | Mailchimp |
| Автоматизация писем | HubSpot |
| Автоматизация поддержки | Intercom |
| Автоматизация через workflow builder | Slack |
| Автоматическое масштабирование | Kubernetes |
| Аналитика трафика | Google Analytics |
| База знаний | Zendesk |
| Боты и help center | Intercom |
| Вебинары | Zoom |
| Видеозвонки в браузере | Google Meet |
| Видеоконференции | Zoom |
| Воронки продаж | HubSpot |
| Встроенные платежи | Shopify |
| Документация команд | Confluence |
| Документы и базы знаний | Notion |
| Запись встреч | Zoom |
| Запись и транскрипция | Google Meet |
| Интеграции с инструментами разработки | Slack |
| Интеграция с календарем | Gmail |
| Интернет-магазин | Shopify |
| Календарь и контакты | Microsoft Outlook |
| Канбан-доски | Trello |
| Командные чаты и каналы | Slack |
| Компонентные библиотеки | Figma |
| Корпоративное управление доступом | Microsoft Teams |
| Корпоративные порталы | SharePoint |
| Напоминания | Google Calendar |
| Общие календари | Google Calendar |
| Омниканальные каналы | Zendesk |
| Онлайн-доски | Miro |
| Онлайн-платежи | Stripe |
| Оркестрация контейнеров | Kubernetes |
| Отчеты и аналитика | Salesforce |
| Отчеты и дашборды | Google Analytics |
| Отчеты по задачам | Jira Software |
| Планирование встреч | Google Calendar |
| Планирование спринтов | Jira Software |
| Подписки и инвойсы | Stripe |
| Поиск по сообщениям и файлам | Slack |
| Репозитории и MR | GitLab |
| Самовосстановление сервисов | Kubernetes |
| Сегментация аудитории | Mailchimp, Google Analytics |
| Совместная работа с файлами | Microsoft Teams |
| Совместное редактирование | Confluence, Figma |
| Совместное рисование | Miro |
| Совместные встречи из календаря | Google Meet |
| Совместные сайты | SharePoint |
| Совместный доступ | Google Drive |
| Таблицы и базы данных | Notion |
| Таймлайны проектов | Asana |
| Тикетинг поддержки | Zendesk |
| Управление бэклогом | Jira Software |
| Управление версиями | Google Drive |
| Управление документами | SharePoint |
| Управление задачами | Asana, Microsoft Outlook |
| Управление каталогом | Shopify |
| Управление лидами | Salesforce |
| Управление рисками | Stripe |
| Управление уязвимостями | GitLab |
| Фильтры и ярлыки | Gmail |
| Хостинг репозиториев | GitHub |
| Хранение файлов | Google Drive |
| Чат с клиентами | Intercom |
| Чаты и видеозвонки | Microsoft Teams |
| Шаблоны воркшопов | Miro |
| Шаблоны проектов | Trello |
| Шаблоны рабочих пространств | Notion |
| Шаблоны рабочих процессов | Asana |
| Шаблоны страниц | Confluence |
| Электронная почта | Gmail, Microsoft Outlook |

## Сверка связей с Function Dictionary

В Function Dictionary включено 81 уникальная функция из каталога. Все функции имеют как минимум один источник (приложение) в таблице «Функция → Приложения», «пустых» функций без источников нет.

## Правила добавления нового приложения

1. **Критерии включения**: приложение должно иметь понятные сценарии использования, актуальные платформы и доступную документацию.
2. **Минимальные данные**: `id`, `name`, `platforms`, `functions`, `limitations`, `price`, `compatibility`, `documentation`, `support_status`, `maturity`, `update_status`, `use_cases`, `licensing`.
3. **Проверки качества**: заполнить 3–7 функций, указать ограничения и ссылку на официальную документацию.
4. **Совместимость**: перечислять только подтвержденные интеграции с `id` из каталога.
5. **Обновляемость**: проставлять `update_status` (active/rare/frozen) на основании частоты релизов.
