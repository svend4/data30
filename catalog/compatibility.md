# Карта совместимости

Источник данных — поле `compatibility` в `apps.yaml`. Ниже приведена читаемая карта интеграций.

| Приложение | Совместимость (id) |
| --- | --- |
| Slack | jira, github, google-meet, zoom |
| Microsoft Teams | jira, zoom, sharepoint, outlook |
| Zoom | slack, microsoft-teams, google-calendar, outlook |
| Google Meet | google-calendar, slack, asana |
| Jira Software | confluence, slack, github, bitbucket |
| Trello | slack, google-drive, jira |
| Asana | slack, google-meet, zoom |
| Notion | slack, google-drive, github |
| Confluence | jira, slack, google-drive |
| GitHub | jira, slack, notion |
| GitLab | jira, slack, kubernetes |
| Bitbucket | jira, confluence |
| Figma | jira, github, notion |
| Miro | slack, zoom, jira |
| Salesforce | slack, zoom, outlook |
| HubSpot | slack, gmail, zoom |
| Zendesk | slack, salesforce, jira |
| Intercom | slack, zendesk, salesforce |
| Stripe | shopify, salesforce, hubspot |
| Shopify | stripe, mailchimp, google-analytics |
| Mailchimp | shopify, salesforce, hubspot |
| Google Drive | google-meet, slack, notion |
| Gmail | hubspot, google-calendar, slack |
| Google Calendar | zoom, google-meet, slack |
| Microsoft Outlook | microsoft-teams, zoom, salesforce |
| SharePoint | microsoft-teams, outlook |
| Kubernetes | gitlab, github |
| Google Analytics | shopify, google-drive |

## Карта зависимостей

Источник данных — поле `dependencies` в `apps.yaml`.

| Приложение | Зависимости |
| --- | --- |
| Slack | — |
| Microsoft Teams | microsoft-365 |
| Zoom | — |
| Google Meet | google-workspace |
| Jira Software | atlassian-cloud |
| Trello | atlassian-cloud |
| Asana | — |
| Notion | — |
| Confluence | atlassian-cloud |
| GitHub | — |
| GitLab | — |
| Bitbucket | atlassian-cloud |
| Figma | — |
| Miro | — |
| Salesforce | — |
| HubSpot | — |
| Zendesk | — |
| Intercom | — |
| Stripe | — |
| Shopify | — |
| Mailchimp | — |
| Google Drive | google-workspace |
| Gmail | google-workspace |
| Google Calendar | google-workspace |
| Microsoft Outlook | microsoft-365 |
| SharePoint | microsoft-365 |
| Kubernetes | container-runtime |
| Google Analytics | google-workspace |
