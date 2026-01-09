# Единый формат карточки приложения

Каждая карточка описывает приложение в каталоге и хранится в `apps.yaml`.

## Поля

- `id` — уникальный идентификатор (slug).
- `name` — название приложения.
- `platforms` — список поддерживаемых платформ (web, ios, android, desktop, cli, api).
- `functions` — ключевые функции (3–7 пунктов).
- `compatibility` — список `id` приложений, с которыми есть проверенная интеграция.
- `support_status` — статус поддержки (active, limited, deprecated, discontinued).
- `maturity` — зрелость (beta, stable, enterprise).
- `use_cases` — сценарии использования (use case) в виде списка.
- `licensing` — сведения о лицензировании и стоимости:
  - `model` — модель лицензирования (open_source, subscription, perpetual, usage_based, freemium).
  - `license` — тип лицензии (например, MIT, Apache-2.0, commercial).
  - `cost` — ориентир стоимости (free, trial, paid, tiered, custom).
  - `notes` — уточнения по условиям.

## Минимальные требования

- Каждая карточка должна содержать все поля.
- `compatibility` не должна содержать собственный `id`.
- Для MVP каталог содержит 20–50 приложений.
