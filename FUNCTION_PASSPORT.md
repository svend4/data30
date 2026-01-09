# Паспорт функций — базовая спецификация и MVP‑словарь

## 1. Минимальная спецификация функции
**Цель:** минимально достаточное описание для использования, оценки и интеграции функции.

**Входы**
- Типы и формат данных (JSON, CSV, строки, бинарные данные).
- Обязательные и опциональные поля.
- Ограничения (размер, диапазон значений).

**Выходы**
- Тип и формат результата.
- Структура ответа и семантика полей.
- Гарантии (детерминированность, стабильность формата).

**Побочные эффекты**
- Запись в хранилища, внешние вызовы, изменение состояния.
- Идемпотентность и условия повторных вызовов.

**Ошибки**
- Классы ошибок (валидация, бизнес‑правила, инфраструктура).
- Коды/типы ошибок и формат описания.
- Поведение при частичном успехе.

## 2. Категории функций
- **Ввод/вывод:** чтение/запись файлов, экспорт/импорт.
- **Трансформация:** преобразование, нормализация, агрегация.
- **Хранение:** операции с БД/объектными хранилищами.
- **Коммуникации:** HTTP/SMTP/очереди/вебхуки.
- **Поиск/извлечение:** фильтрация, поиск, ML‑retrieval.
- **Валидация/качество:** проверка схем, дедупликация.
- **Безопасность:** шифрование, маскирование, аудит.
- **Оркестрация:** планирование, запуск пайплайнов.

## 3. Метаданные
- **Зрелость:** draft / beta / stable / deprecated.
- **Цена:** free / paid + модель (per call, per GB, per user).
- **Совместимость:** версии API, поддерживаемые форматы и SDK.
- **Статус поддержки:** active / limited / deprecated / discontinued.
- **Ограничения:** лимиты размера, RPS, квоты.
- **SLA:** доступность, латентность, время восстановления.

## 4. Шаблон паспорта функции

### Табличный вид
| Поле | Описание |
| --- | --- |
| Имя | Уникальный идентификатор функции |
| Назначение | Что делает функция |
| Категория | Ввод/вывод, Трансформация, Хранение, Коммуникации и т.д. |
| Входы | Типы, формат, обязательность |
| Выходы | Типы, формат |
| Побочные эффекты | Запись/вызовы/изменение состояния |
| Ошибки | Коды, форматы, условия |
| Ограничения | Лимиты, квоты, RPS |
| Зрелость | draft/beta/stable/deprecated |
| Цена | Модель тарификации |
| Совместимость | Версии API, SDK, форматы |
| Статус поддержки | active/limited/deprecated/discontinued |
| SLA | Доступность, латентность |
| Примечания | Доп. сведения |

### JSON
```json
{
  "name": "normalize_phone",
  "purpose": "Normalize phone numbers to E.164",
  "category": "transformation",
  "inputs": {
    "phone": "string",
    "default_country": "string (ISO-2)"
  },
  "outputs": {
    "normalized": "string",
    "is_valid": "boolean"
  },
  "side_effects": "none",
  "errors": [
    {"code": "VALIDATION_ERROR", "message": "invalid input"}
  ],
  "limits": {"max_length": 64, "rps": 100},
  "maturity": "beta",
  "pricing": "free",
  "compatibility": {"api_versions": ["v1"], "formats": ["json"]},
  "support_status": "active",
  "sla": {"availability": "99.9%", "latency_p95_ms": 200},
  "notes": "Uses libphonenumber rules"
}
```

### YAML
```yaml
name: normalize_phone
purpose: Normalize phone numbers to E.164
category: transformation
inputs:
  phone: string
  default_country: string (ISO-2)
outputs:
  normalized: string
  is_valid: boolean
side_effects: none
errors:
  - code: VALIDATION_ERROR
    message: invalid input
limits:
  max_length: 64
  rps: 100
maturity: beta
pricing: free
compatibility:
  api_versions: [v1]
  formats: [json]
support_status: active
sla:
  availability: 99.9%
  latency_p95_ms: 200
notes: Uses libphonenumber rules
```

## 5. MVP‑словарь функций (60 шт.)

**Статус зрелости:** все ключевые функции в MVP фиксируются на уровне `beta`.

| Функция | Категория | Описание | Пример входа | Пример выхода |
| --- | --- | --- | --- | --- |
| read_csv | ввод/вывод | Чтение CSV в табличную структуру | `{"path":"/data/file.csv"}` | `{"rows":1200}` |
| write_csv | ввод/вывод | Запись таблицы в CSV | `{"rows":1200,"path":"/out.csv"}` | `{"status":"ok"}` |
| read_json | ввод/вывод | Чтение JSON файла | `{"path":"/data/file.json"}` | `{"keys":12}` |
| write_json | ввод/вывод | Запись JSON | `{"data":{},"path":"/out.json"}` | `{"status":"ok"}` |
| read_parquet | ввод/вывод | Чтение Parquet | `{"path":"/data/file.parquet"}` | `{"rows":50000}` |
| write_parquet | ввод/вывод | Запись Parquet | `{"rows":50000,"path":"/out.parquet"}` | `{"status":"ok"}` |
| normalize_phone | трансформация | Нормализация телефонов | `{"phone":"+7 999 123-45-67"}` | `{"normalized":"+79991234567"}` |
| normalize_email | трансформация | Очистка email (lowercase, trim) | `{"email":" User@Example.com "}` | `{"normalized":"user@example.com"}` |
| parse_date | трансформация | Разбор даты в ISO | `{"date":"01.12.2024"}` | `{"iso":"2024-12-01"}` |
| format_date | трансформация | Форматирование ISO даты | `{"iso":"2024-12-01"}` | `{"date":"01.12.2024"}` |
| to_uppercase | трансформация | Перевод строк в верхний регистр | `{"text":"hello"}` | `{"text":"HELLO"}` |
| to_lowercase | трансформация | Перевод строк в нижний регистр | `{"text":"Hello"}` | `{"text":"hello"}` |
| trim_whitespace | трансформация | Удаление пробелов по краям | `{"text":"  hi "}` | `{"text":"hi"}` |
| replace_regex | трансформация | Замена по regex | `{"text":"a1","pattern":"\\d","replace":""}` | `{"text":"a"}` |
| split_string | трансформация | Разделение строки по разделителю | `{"text":"a,b","sep":","}` | `{"parts":["a","b"]}` |
| join_strings | трансформация | Склейка строк с разделителем | `{"parts":["a","b"],"sep":","}` | `{"text":"a,b"}` |
| hash_sha256 | безопасность | Хэширование SHA‑256 | `{"text":"secret"}` | `{"hash":"..."}` |
| encrypt_aes | безопасность | Шифрование AES | `{"data":"...","key":"k"}` | `{"cipher":"..."}` |
| decrypt_aes | безопасность | Дешифрование AES | `{"cipher":"...","key":"k"}` | `{"data":"..."}` |
| mask_pii | безопасность | Маскирование PII | `{"text":"email@example.com"}` | `{"text":"e***@example.com"}` |
| validate_json_schema | валидация | Проверка JSON по схеме | `{"data":{},"schema":{}}` | `{"valid":true}` |
| validate_email | валидация | Проверка email | `{"email":"a@b.com"}` | `{"valid":true}` |
| validate_phone | валидация | Проверка телефона | `{"phone":"+79991234567"}` | `{"valid":true}` |
| deduplicate_rows | качество | Удаление дублей по ключам | `{"keys":["id"]}` | `{"removed":12}` |
| detect_nulls | качество | Поиск null/пустых значений | `{"columns":["name"]}` | `{"nulls":15}` |
| fill_missing | качество | Заполнение пропусков | `{"strategy":"mean"}` | `{"filled":15}` |
| filter_rows | поиск/извлечение | Фильтрация по условию | `{"where":"age>18"}` | `{"rows":120}` |
| sort_rows | поиск/извлечение | Сортировка по полям | `{"by":["date"]}` | `{"rows":1200}` |
| group_by | трансформация | Группировка и агрегаты | `{"by":["city"],"agg":"count"}` | `{"rows":20}` |
| aggregate_sum | трансформация | Сумма по колонке | `{"column":"amount"}` | `{"sum":12345}` |
| aggregate_avg | трансформация | Среднее по колонке | `{"column":"amount"}` | `{"avg":123.45}` |
| pivot_table | трансформация | Поворот таблицы | `{"index":"month","columns":"city"}` | `{"rows":12}` |
| unpivot_table | трансформация | Распаковка широкой таблицы | `{"columns":["m1","m2"]}` | `{"rows":240}` |
| join_tables | трансформация | Соединение таблиц | `{"left":"a","right":"b","on":["id"]}` | `{"rows":500}` |
| merge_datasets | трансформация | Объединение наборов | `{"inputs":["a","b"]}` | `{"rows":2000}` |
| calculate_percentile | аналитика | Перцентиль | `{"column":"amount","p":0.95}` | `{"value":999}` |
| calculate_zscore | аналитика | Z‑score | `{"value":10,"mean":5,"std":2}` | `{"z":2.5}` |
| normalize_minmax | аналитика | Min‑Max нормализация | `{"min":0,"max":100,"value":10}` | `{"scaled":0.1}` |
| tokenize_text | трансформация | Токенизация текста | `{"text":"hello world"}` | `{"tokens":["hello","world"]}` |
| stem_text | трансформация | Стемминг | `{"tokens":["running"]}` | `{"tokens":["run"]}` |
| detect_language | аналитика | Определение языка | `{"text":"Привет"}` | `{"lang":"ru"}` |
| translate_text | коммуникации | Перевод текста | `{"text":"Hello","to":"ru"}` | `{"text":"Привет"}` |
| send_email | коммуникации | Отправка email | `{"to":"a@b.com","subject":"Hi"}` | `{"status":"sent"}` |
| send_sms | коммуникации | Отправка SMS | `{"to":"+7999...","text":"Hi"}` | `{"status":"sent"}` |
| call_webhook | коммуникации | Вызов вебхука | `{"url":"https://...","payload":{}}` | `{"status":200}` |
| http_get | коммуникации | HTTP GET | `{"url":"https://..."}` | `{"status":200}` |
| http_post | коммуникации | HTTP POST | `{"url":"https://...","body":{}}` | `{"status":201}` |
| publish_queue | коммуникации | Публикация в очередь | `{"topic":"events","message":{}}` | `{"offset":123}` |
| consume_queue | коммуникации | Чтение из очереди | `{"topic":"events"}` | `{"messages":10}` |
| create_table | хранение | Создание таблицы | `{"name":"users","schema":{}}` | `{"status":"ok"}` |
| insert_rows | хранение | Вставка строк | `{"table":"users","rows":10}` | `{"inserted":10}` |
| update_rows | хранение | Обновление строк | `{"table":"users","where":"id=1"}` | `{"updated":1}` |
| delete_rows | хранение | Удаление строк | `{"table":"users","where":"id=1"}` | `{"deleted":1}` |
| query_sql | хранение | SQL‑запрос | `{"sql":"SELECT 1"}` | `{"rows":1}` |
| export_s3 | хранение | Экспорт в S3 | `{"bucket":"b","path":"/out"}` | `{"status":"ok"}` |
| import_s3 | хранение | Импорт из S3 | `{"bucket":"b","path":"/in"}` | `{"rows":500}` |
| create_index | хранение | Создание индекса | `{"table":"users","column":"email"}` | `{"status":"ok"}` |
| backup_dataset | хранение | Бэкап набора | `{"dataset":"users"}` | `{"status":"ok"}` |
| restore_dataset | хранение | Восстановление | `{"backup_id":"b1"}` | `{"status":"ok"}` |
| schedule_job | оркестрация | Планирование задачи | `{"cron":"0 1 * * *"}` | `{"job_id":"j1"}` |
| run_pipeline | оркестрация | Запуск пайплайна | `{"pipeline":"daily"}` | `{"run_id":"r1"}` |
| cancel_job | оркестрация | Отмена задачи | `{"job_id":"j1"}` | `{"status":"canceled"}` |
| get_job_status | оркестрация | Статус выполнения | `{"job_id":"j1"}` | `{"status":"running"}` |
| track_event | аналитика | Отслеживание события | `{"event":"signup"}` | `{"status":"ok"}` |
| calculate_retention | аналитика | Расчет ретенции | `{"cohort":"2024-01"}` | `{"retention":0.42}` |
| recommend_items | аналитика | Рекомендации товаров | `{"user_id":"u1"}` | `{"items":["i1"]}` |
| search_text | поиск/извлечение | Полнотекстовый поиск | `{"query":"data"}` | `{"rows":12}` |
| geo_enrich | аналитика | Геокодирование | `{"address":"Москва"}` | `{"lat":55.75,"lon":37.61}` |
| classify_text | аналитика | Классификация текста | `{"text":"spam"}` | `{"label":"spam"}` |
| extract_entities | аналитика | Извлечение сущностей | `{"text":"Иван в Москве"}` | `{"entities":["Иван","Москва"]}` |
| detect_outliers | качество | Поиск выбросов | `{"column":"amount"}` | `{"outliers":5}` |
| compute_checksum | безопасность | Контрольная сумма | `{"data":"..."}` | `{"checksum":"..."}` |
| generate_report | ввод/вывод | Генерация отчета | `{"template":"monthly"}` | `{"path":"/reports/m.pdf"}` |

## 6. Ревизия пересечений и дублей
- **read_csv / read_parquet / read_json**: одинаковая семантика чтения, различие только в формате. Возможна унификация через `read_file(format=...)`.
- **write_csv / write_parquet / write_json**: аналогично, можно объединить через `write_file(format=...)`.
- **normalize_phone / validate_phone**: уместно объединить в `parse_phone` с флагами валидации и нормализации.
- **normalize_email / validate_email**: возможен `parse_email` с опцией очистки.
- **http_get / http_post / call_webhook**: унификация в `http_request(method=...)`.
- **aggregate_sum / aggregate_avg / group_by**: может быть единая `aggregate` с параметрами.
- **create_table / create_index**: общий интерфейс управления схемой (schema management).
- **export_s3 / import_s3**: общий `s3_transfer(direction=...)`.
- **backup_dataset / restore_dataset**: общий `dataset_backup(action=...)`.
- **schedule_job / run_pipeline / cancel_job / get_job_status**: общий API управления задачами.
