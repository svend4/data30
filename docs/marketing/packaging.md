# Пакеты сервиса и условия предоставления

Документ основан на полях паспорта функции: `limits`, `SLA`, `pricing` (см. FUNCTION_PASSPORT.md).

## Уровни сервиса (limits / SLA / pricing)

### Free
- **Pricing:** бесплатно.
- **Limits:** до 5 RPS, до 50 000 вызовов/мес, размер запроса до 256 КБ.
- **SLA:** best‑effort, целевая доступность 99.0%, p95 ≤ 800 мс.
- **Поддержка:** community‑канал, ответы по мере возможности.
- **Включено:** базовые функции ввода/вывода и трансформаций, без расширенной аналитики.

### Pro
- **Pricing:** подписка + перерасход по факту (per call).
- **Limits:** до 50 RPS, до 2 000 000 вызовов/мес, размер запроса до 2 МБ.
- **SLA:** 99.5% доступности, p95 ≤ 400 мс, восстановление ≤ 4 часа.
- **Поддержка:** e‑mail, 8×5, реакция до 1 рабочего дня.
- **Включено:** полный набор MVP‑функций, приоритет в очередях.

### Enterprise
- **Pricing:** индивидуальный контракт, per call/per month, скидки на объем.
- **Limits:** от 200 RPS, квоты по договору, размер запроса до 10 МБ.
- **SLA:** 99.9% доступности, p95 ≤ 200 мс, восстановление ≤ 1 час.
- **Поддержка:** выделенный менеджер, 24×7, реакция до 1 часа.
- **Включено:** расширенные интеграции, кастомные лимиты, аудит и отчеты.

## Trial / POC условия

### Trial (14 дней)
- **Срок:** 14 календарных дней.
- **Limits:** до 3 RPS, до 10 000 вызовов за период, размер запроса до 128 КБ.
- **SLA:** best‑effort.
- **Список функций (MVP‑словарь):**
  - read_csv, write_csv
  - read_json, write_json
  - normalize_email, normalize_phone
  - validate_email, validate_phone
  - trim_whitespace, to_lowercase
  - hash_sha256, mask_pii

### POC (30 дней)
- **Срок:** до 30 календарных дней.
- **Limits:** до 10 RPS, до 200 000 вызовов за период, размер запроса до 512 КБ.
- **SLA:** 99.0% доступности, p95 ≤ 800 мс.
- **Список функций (MVP‑словарь):**
  - read_csv, write_csv, read_json, write_json, read_parquet, write_parquet
  - normalize_phone, normalize_email, parse_date, format_date
  - validate_json_schema, validate_email, validate_phone
  - deduplicate_rows, detect_nulls, fill_missing
  - filter_rows, sort_rows, group_by, aggregate_sum, aggregate_avg
  - http_get, http_post, call_webhook
  - create_table, insert_rows, update_rows, delete_rows, query_sql

## Примечания по лимитам и квотам
- Лимиты RPS и месячные/периодические квоты задаются на уровне API‑ключа.
- При достижении квоты ответы возвращают ошибку лимита и рекомендации по апгрейду.
- SLA и поддержка применяются согласно активному пакету (pricing‑уровню).
