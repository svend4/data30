# Шаблон карточки приложения

Этот шаблон используется для добавления новых приложений в `catalog/apps.yaml`.

```yaml
- id: "app-id"
  name: "Название приложения"
  platforms: [web, ios, android]
  functions:
    - "Ключевая функция 1"
    - "Ключевая функция 2"
    - "Ключевая функция 3"
  compatibility: [related-app-id-1, related-app-id-2]
  support_status: active
  maturity: stable
  use_cases:
    - "Основной сценарий 1"
    - "Основной сценарий 2"
  licensing:
    model: subscription
    license: commercial
    cost: tiered
    notes: "Краткое описание модели лицензирования."
```

## Проверочный список

1. `id` уникален и соответствует slug формату.
2. В `platforms` указаны только поддерживаемые значения (web, ios, android, desktop, cli, api).
3. В `functions` описано 3–7 ключевых функций.
4. `compatibility` не включает собственный `id`.
5. `support_status` и `maturity` соответствуют допустимым значениям в `catalog/schema.md`.
6. `use_cases` описывают сценарии, а не технические детали.
7. Поле `licensing` заполнено полностью.
