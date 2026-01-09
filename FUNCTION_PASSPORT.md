# Паспорт функций — базовая спецификация и MVP‑словарь

## 1. Паспорт функции (утвержденный состав полей)
**Цель:** единый минимальный набор полей для описания функций в каталоге и интеграциях.

**Обязательные поля паспорта**
- **ID** — уникальный идентификатор (например, `F042`).
- **Имя** — нормализованное имя функции (snake_case, глагол + объект).
- **Категория** — одна из базовых категорий (см. раздел 2).
- **Входы** — типы и форматы данных, обязательность, ограничения по размеру/диапазону.
- **Выходы** — типы и формат результата, структура и семантика полей.
- **Ошибки** — классы и коды ошибок, формат сообщения, условия возникновения.
- **Ограничения** — лимиты размера, RPS/квоты, совместимость.
- **Пример** — минимум один пример входа и выхода.

## 2. Категории функций (базовые)
- **Ввод/вывод** — чтение/запись файлов, сериализация, импорт/экспорт.
- **Трансформация** — преобразование, очистка, нормализация, агрегация.
- **Хранение** — операции с БД, таблицами, индексами, бэкапами.
- **Коммуникации** — HTTP/SMTP/очереди/уведомления/вебхуки.
- **Аналитика** — метрики, статистика, ML‑функции, поиск/рекомендации.

> Допускаются подкатегории (валидация, качество данных, безопасность) как **метки**, но базовая категория должна быть одной из пяти выше.

## 3. Метаданные (рекомендуемые)
- **Зрелость:** draft / beta / stable / deprecated.
- **Цена:** free / paid + модель (per call, per GB, per user).
- **Совместимость:** версии API, поддерживаемые форматы и SDK.
- **Ограничения:** лимиты размера, RPS, квоты.
- **SLA:** доступность, латентность, время восстановления.

## 4. Шаблон паспорта функции

### Табличный вид
| Поле | Описание |
| --- | --- |
| ID | Уникальный идентификатор функции |
| Имя | Нормализованное имя функции |
| Категория | Ввод/вывод, Трансформация, Хранение, Коммуникации, Аналитика |
| Входы | Типы, формат, обязательность |
| Выходы | Типы, формат |
| Ошибки | Коды, форматы, условия |
| Ограничения | Лимиты, квоты, RPS, совместимость |
| Пример | Пример входа и выхода |
| Метки | Доп. классификация (валидация, качество, безопасность) |
| Зрелость | draft/beta/stable/deprecated |
| Цена | Модель тарификации |
| Совместимость | Версии API, SDK, форматы |
| SLA | Доступность, латентность |
| Примечания | Доп. сведения |

### JSON
```json
{
  "id": "F016",
  "name": "normalize_phone",
  "category": "transformation",
  "inputs": {
    "phone": "string",
    "default_country": "string (ISO-2)"
  },
  "outputs": {
    "normalized": "string",
    "is_valid": "boolean"
  },
  "errors": [
    {"code": "VALIDATION_ERROR", "message": "invalid input"}
  ],
  "constraints": {"max_length": 64, "rps": 100, "formats": ["json"]},
  "example": {
    "input": {"phone": "+7 999 123-45-67", "default_country": "RU"},
    "output": {"normalized": "+79991234567", "is_valid": true}
  },
  "tags": ["validation"],
  "maturity": "beta",
  "pricing": "free",
  "compatibility": {"api_versions": ["v1"], "formats": ["json"]},
  "sla": {"availability": "99.9%", "latency_p95_ms": 200},
  "notes": "Uses libphonenumber rules"
}
```

### YAML
```yaml
id: F016
name: normalize_phone
category: transformation
inputs:
  phone: string
  default_country: string (ISO-2)
outputs:
  normalized: string
  is_valid: boolean
errors:
  - code: VALIDATION_ERROR
    message: invalid input
constraints:
  max_length: 64
  rps: 100
  formats: [json]
example:
  input:
    phone: "+7 999 123-45-67"
    default_country: RU
  output:
    normalized: "+79991234567"
    is_valid: true
tags: [validation]
maturity: beta
pricing: free
compatibility:
  api_versions: [v1]
  formats: [json]
sla:
  availability: 99.9%
  latency_p95_ms: 200
notes: Uses libphonenumber rules
```

## 5. MVP‑словарь функций (100 шт., нормализованные названия)

| ID | Функция | Категория | Описание | Пример входа | Пример выхода |
| --- | --- | --- | --- | --- | --- |
| F001 | read_file | ввод/вывод | Чтение файла по пути | `{"path":"/data/file.csv"}` | `{"bytes":1024}` |
| F002 | write_file | ввод/вывод | Запись данных в файл | `{"path":"/out.bin","bytes":1024}` | `{"status":"ok"}` |
| F003 | parse_csv | ввод/вывод | Разбор CSV в таблицу | `{"text":"a,b\n1,2"}` | `{"rows":1}` |
| F004 | parse_json | ввод/вывод | Разбор JSON строки | `{"text":"{\"a\":1}"}` | `{"keys":1}` |
| F005 | parse_xml | ввод/вывод | Разбор XML строки | `{"text":"<a>1</a>"}` | `{"nodes":1}` |
| F006 | parse_yaml | ввод/вывод | Разбор YAML строки | `{"text":"a: 1"}` | `{"keys":1}` |
| F007 | parse_excel | ввод/вывод | Разбор XLSX в таблицу | `{"path":"/data/s.xlsx"}` | `{"sheets":2}` |
| F008 | parse_parquet | ввод/вывод | Разбор Parquet | `{"path":"/data/s.parquet"}` | `{"rows":500}` |
| F009 | serialize_csv | ввод/вывод | Сериализация таблицы в CSV | `{"rows":10}` | `{"text":"..."}` |
| F010 | serialize_json | ввод/вывод | Сериализация объекта в JSON | `{"data":{}}` | `{"text":"{}"}` |
| F011 | serialize_xml | ввод/вывод | Сериализация в XML | `{"data":{}}` | `{"text":"<root/>"}` |
| F012 | serialize_yaml | ввод/вывод | Сериализация в YAML | `{"data":{}}` | `{"text":"{}"}` |
| F013 | serialize_excel | ввод/вывод | Сериализация в XLSX | `{"rows":10}` | `{"path":"/out.xlsx"}` |
| F014 | serialize_parquet | ввод/вывод | Сериализация в Parquet | `{"rows":10}` | `{"path":"/out.parquet"}` |
| F015 | convert_encoding | трансформация | Преобразование кодировки | `{"text":"...","from":"cp1251","to":"utf-8"}` | `{"text":"..."}` |
| F016 | normalize_phone | трансформация | Нормализация телефона | `{"phone":"+7 999 123-45-67"}` | `{"normalized":"+79991234567"}` |
| F017 | normalize_email | трансформация | Очистка email | `{"email":" User@Example.com "}` | `{"normalized":"user@example.com"}` |
| F018 | parse_date | трансформация | Разбор даты в ISO | `{"date":"01.12.2024"}` | `{"iso":"2024-12-01"}` |
| F019 | format_date | трансформация | Форматирование ISO даты | `{"iso":"2024-12-01"}` | `{"date":"01.12.2024"}` |
| F020 | to_uppercase | трансформация | Приведение к верхнему регистру | `{"text":"hello"}` | `{"text":"HELLO"}` |
| F021 | to_lowercase | трансформация | Приведение к нижнему регистру | `{"text":"Hello"}` | `{"text":"hello"}` |
| F022 | trim_whitespace | трансформация | Удаление пробелов по краям | `{"text":"  hi "}` | `{"text":"hi"}` |
| F023 | replace_regex | трансформация | Замена по regex | `{"text":"a1","pattern":"\\d"}` | `{"text":"a"}` |
| F024 | split_string | трансформация | Разделение строки | `{"text":"a,b","sep":","}` | `{"parts":["a","b"]}` |
| F025 | join_strings | трансформация | Склейка строк | `{"parts":["a","b"],"sep":","}` | `{"text":"a,b"}` |
| F026 | slugify_text | трансформация | Генерация slug | `{"text":"Hello World"}` | `{"slug":"hello-world"}` |
| F027 | remove_html | трансформация | Удаление HTML-тегов | `{"text":"<b>a</b>"}` | `{"text":"a"}` |
| F028 | tokenize_text | трансформация | Токенизация текста | `{"text":"hello world"}` | `{"tokens":["hello","world"]}` |
| F029 | stem_text | трансформация | Стемминг | `{"tokens":["running"]}` | `{"tokens":["run"]}` |
| F030 | lemmatize_text | трансформация | Лемматизация | `{"tokens":["better"]}` | `{"tokens":["good"]}` |
| F031 | detect_language | аналитика | Определение языка | `{"text":"Привет"}` | `{"lang":"ru"}` |
| F032 | translate_text | коммуникации | Перевод текста | `{"text":"Hello","to":"ru"}` | `{"text":"Привет"}` |
| F033 | classify_text | аналитика | Классификация текста | `{"text":"spam"}` | `{"label":"spam"}` |
| F034 | extract_entities | аналитика | Извлечение сущностей | `{"text":"Иван в Москве"}` | `{"entities":["Иван","Москва"]}` |
| F035 | sentiment_analysis | аналитика | Анализ тональности | `{"text":"Отлично"}` | `{"sentiment":"positive"}` |
| F036 | summarize_text | аналитика | Краткое резюме текста | `{"text":"Длинный текст"}` | `{"summary":"..."}` |
| F037 | detect_toxicity | аналитика | Детекция токсичности | `{"text":"..."}` | `{"toxic":false}` |
| F038 | hash_sha256 | трансформация | Хэширование SHA‑256 | `{"text":"secret"}` | `{"hash":"..."}` |
| F039 | compute_checksum | трансформация | Контрольная сумма | `{"data":"..."}` | `{"checksum":"..."}` |
| F040 | encrypt_aes | трансформация | Шифрование AES | `{"data":"...","key":"k"}` | `{"cipher":"..."}` |
| F041 | decrypt_aes | трансформация | Дешифрование AES | `{"cipher":"...","key":"k"}` | `{"data":"..."}` |
| F042 | sign_hmac | трансформация | Подпись HMAC | `{"data":"...","key":"k"}` | `{"signature":"..."}` |
| F043 | verify_hmac | трансформация | Проверка HMAC | `{"data":"...","signature":"..."}` | `{"valid":true}` |
| F044 | mask_pii | трансформация | Маскирование PII | `{"text":"email@example.com"}` | `{"text":"e***@example.com"}` |
| F045 | redact_pii | трансформация | Удаление PII | `{"text":"..."}` | `{"text":"[REDACTED]"}` |
| F046 | validate_json_schema | трансформация | Валидация JSON по схеме | `{"data":{},"schema":{}}` | `{"valid":true}` |
| F047 | validate_email | трансформация | Проверка email | `{"email":"a@b.com"}` | `{"valid":true}` |
| F048 | validate_phone | трансформация | Проверка телефона | `{"phone":"+7999"}` | `{"valid":true}` |
| F049 | validate_uuid | трансформация | Проверка UUID | `{"uuid":"..."}` | `{"valid":true}` |
| F050 | validate_range | трансформация | Проверка диапазона | `{"value":10,"min":0,"max":100}` | `{"valid":true}` |
| F051 | detect_nulls | трансформация | Поиск null/пустых значений | `{"columns":["name"]}` | `{"nulls":15}` |
| F052 | fill_missing | трансформация | Заполнение пропусков | `{"strategy":"mean"}` | `{"filled":15}` |
| F053 | deduplicate_rows | трансформация | Удаление дублей по ключам | `{"keys":["id"]}` | `{"removed":12}` |
| F054 | detect_outliers | аналитика | Поиск выбросов | `{"column":"amount"}` | `{"outliers":5}` |
| F055 | filter_rows | трансформация | Фильтрация по условию | `{"where":"age>18"}` | `{"rows":120}` |
| F056 | sort_rows | трансформация | Сортировка по полям | `{"by":["date"]}` | `{"rows":1200}` |
| F057 | group_by | трансформация | Группировка и агрегаты | `{"by":["city"],"agg":"count"}` | `{"rows":20}` |
| F058 | aggregate_sum | трансформация | Сумма по колонке | `{"column":"amount"}` | `{"sum":12345}` |
| F059 | aggregate_avg | трансформация | Среднее по колонке | `{"column":"amount"}` | `{"avg":123.45}` |
| F060 | aggregate_min | трансформация | Минимум по колонке | `{"column":"amount"}` | `{"min":1}` |
| F061 | aggregate_max | трансформация | Максимум по колонке | `{"column":"amount"}` | `{"max":999}` |
| F062 | calculate_percentile | аналитика | Перцентиль | `{"column":"amount","p":0.95}` | `{"value":999}` |
| F063 | calculate_zscore | аналитика | Z‑score | `{"value":10,"mean":5,"std":2}` | `{"z":2.5}` |
| F064 | normalize_minmax | трансформация | Min‑Max нормализация | `{"min":0,"max":100,"value":10}` | `{"scaled":0.1}` |
| F065 | pivot_table | трансформация | Поворот таблицы | `{"index":"month","columns":"city"}` | `{"rows":12}` |
| F066 | unpivot_table | трансформация | Распаковка широкой таблицы | `{"columns":["m1","m2"]}` | `{"rows":240}` |
| F067 | join_tables | трансформация | Соединение таблиц | `{"left":"a","right":"b","on":["id"]}` | `{"rows":500}` |
| F068 | merge_datasets | трансформация | Объединение наборов | `{"inputs":["a","b"]}` | `{"rows":2000}` |
| F069 | calculate_correlation | аналитика | Корреляция между колонками | `{"x":"a","y":"b"}` | `{"corr":0.7}` |
| F070 | compute_trend | аналитика | Расчет тренда | `{"series":[1,2,3]}` | `{"trend":"up"}` |
| F071 | forecast_timeseries | аналитика | Прогноз временного ряда | `{"series":[1,2,3],"horizon":3}` | `{"forecast":[4,5,6]}` |
| F072 | recommend_items | аналитика | Рекомендации товаров | `{"user_id":"u1"}` | `{"items":["i1"]}` |
| F073 | search_text | аналитика | Полнотекстовый поиск | `{"query":"data"}` | `{"rows":12}` |
| F074 | geo_enrich | аналитика | Геокодирование | `{"address":"Москва"}` | `{"lat":55.75,"lon":37.61}` |
| F075 | calculate_retention | аналитика | Расчет ретенции | `{"cohort":"2024-01"}` | `{"retention":0.42}` |
| F076 | track_event | аналитика | Отслеживание события | `{"event":"signup"}` | `{"status":"ok"}` |
| F077 | generate_report | ввод/вывод | Генерация отчета | `{"template":"monthly"}` | `{"path":"/reports/m.pdf"}` |
| F078 | create_table | хранение | Создание таблицы | `{"name":"users","schema":{}}` | `{"status":"ok"}` |
| F079 | drop_table | хранение | Удаление таблицы | `{"name":"users"}` | `{"status":"ok"}` |
| F080 | create_index | хранение | Создание индекса | `{"table":"users","column":"email"}` | `{"status":"ok"}` |
| F081 | create_view | хранение | Создание представления | `{"name":"v_users","sql":"..."}` | `{"status":"ok"}` |
| F082 | list_tables | хранение | Список таблиц | `{"schema":"public"}` | `{"tables":["users"]}` |
| F083 | get_schema | хранение | Получение схемы | `{"table":"users"}` | `{"columns":5}` |
| F084 | query_sql | хранение | SQL‑запрос | `{"sql":"SELECT 1"}` | `{"rows":1}` |
| F085 | insert_rows | хранение | Вставка строк | `{"table":"users","rows":10}` | `{"inserted":10}` |
| F086 | update_rows | хранение | Обновление строк | `{"table":"users","where":"id=1"}` | `{"updated":1}` |
| F087 | delete_rows | хранение | Удаление строк | `{"table":"users","where":"id=1"}` | `{"deleted":1}` |
| F088 | upsert_rows | хранение | Upsert строк | `{"table":"users","rows":10}` | `{"upserted":10}` |
| F089 | backup_dataset | хранение | Бэкап набора | `{"dataset":"users"}` | `{"status":"ok"}` |
| F090 | restore_dataset | хранение | Восстановление | `{"backup_id":"b1"}` | `{"status":"ok"}` |
| F091 | export_object_storage | ввод/вывод | Экспорт в объектное хранилище | `{"bucket":"b","path":"/out"}` | `{"status":"ok"}` |
| F092 | import_object_storage | ввод/вывод | Импорт из объектного хранилища | `{"bucket":"b","path":"/in"}` | `{"rows":500}` |
| F093 | http_request | коммуникации | HTTP запрос | `{"method":"GET","url":"https://..."}` | `{"status":200}` |
| F094 | send_email | коммуникации | Отправка email | `{"to":"a@b.com","subject":"Hi"}` | `{"status":"sent"}` |
| F095 | send_sms | коммуникации | Отправка SMS | `{"to":"+7999...","text":"Hi"}` | `{"status":"sent"}` |
| F096 | send_push | коммуникации | Push‑уведомление | `{"to":"device","text":"Hi"}` | `{"status":"sent"}` |
| F097 | publish_queue | коммуникации | Публикация в очередь | `{"topic":"events","message":{}}` | `{"offset":123}` |
| F098 | consume_queue | коммуникации | Чтение из очереди | `{"topic":"events"}` | `{"messages":10}` |
| F099 | schedule_job | коммуникации | Планирование задачи | `{"cron":"0 1 * * *"}` | `{"job_id":"j1"}` |
| F100 | run_pipeline | коммуникации | Запуск пайплайна | `{"pipeline":"daily"}` | `{"run_id":"r1"}` |

## 6. Ревизия дублей и синонимов (нормализация)
- **read_* / write_* / import_* / export_*** → нормализовано в `read_file`, `write_file`, `import_object_storage`, `export_object_storage` с параметрами формата и хранилища.
- **http_get / http_post / call_webhook** → нормализовано в `http_request(method=...)`.
- **normalize_email / validate_email** → оставлены как отдельные (разные цели), но проверка/нормализация могут быть реализованы через единый модуль `email_utils`.
- **normalize_phone / validate_phone** → аналогично, допускается общий низкоуровневый парсер телефона.

## 7. MVP‑словарь и внутренняя ревизия
**MVP‑словарь**: 100 функций (раздел 5) соответствует базовым категориям и нормализованным именам.

**Внутренняя ревизия (чек‑лист)**
- [x] Поля паспорта включают ID, имя, категорию, входы/выходы, ошибки, ограничения, пример.
- [x] Категории сведены к 5 базовым (ввод/вывод, трансформация, хранение, коммуникации, аналитика).
- [x] Подготовлены шаблоны (таблица + JSON/YAML).
- [x] Список расширен до 100 функций и нормализован.
- [x] Дубли и синонимы проверены и сведены к базовым именам.
