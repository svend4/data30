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
- **Ввод/вывод:** чтение/запись файлов, импорт/экспорт.
- **Трансформация:** преобразование, нормализация, агрегирование.
- **Хранение:** операции с БД и объектными хранилищами.
- **Коммуникации:** HTTP/SMTP/очереди/вебхуки.
- **Аналитика:** статистика, моделирование, ML‑операции.

## 3. Метаданные
- **Зрелость:** draft / beta / stable / deprecated.
- **Цена:** free / paid + модель (per call, per GB, per user).
- **Совместимость:** версии API, поддерживаемые форматы и SDK.
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
sla:
  availability: 99.9%
  latency_p95_ms: 200
notes: Uses libphonenumber rules
```

## 5. Словарь функций (100 шт.)

| ID | Название | Категория | Краткое описание |
| --- | --- | --- | --- |
| F001 | read_csv | ввод/вывод | Чтение CSV файла в табличную структуру. |
| F002 | write_csv | ввод/вывод | Запись табличных данных в CSV файл. |
| F003 | read_json | ввод/вывод | Чтение JSON файла в объектную структуру. |
| F004 | write_json | ввод/вывод | Запись объектных данных в JSON файл. |
| F005 | read_parquet | ввод/вывод | Чтение Parquet файла в таблицу. |
| F006 | write_parquet | ввод/вывод | Запись таблицы в Parquet файл. |
| F007 | read_excel | ввод/вывод | Чтение Excel листа в таблицу. |
| F008 | write_excel | ввод/вывод | Запись таблицы в Excel файл. |
| F009 | read_xml | ввод/вывод | Чтение XML файла в структуру данных. |
| F010 | write_xml | ввод/вывод | Запись структуры данных в XML файл. |
| F011 | read_yaml | ввод/вывод | Чтение YAML файла в структуру данных. |
| F012 | write_yaml | ввод/вывод | Запись структуры данных в YAML файл. |
| F013 | read_text | ввод/вывод | Чтение текстового файла в строку. |
| F014 | write_text | ввод/вывод | Запись строки в текстовый файл. |
| F015 | read_binary | ввод/вывод | Чтение бинарного файла в байтовый массив. |
| F016 | write_binary | ввод/вывод | Запись байтового массива в бинарный файл. |
| F017 | load_image | ввод/вывод | Загрузка изображения в объект изображения. |
| F018 | save_image | ввод/вывод | Сохранение изображения в файл. |
| F019 | export_pdf_report | ввод/вывод | Экспорт отчета в PDF файл. |
| F020 | import_zip | ввод/вывод | Импорт данных из ZIP архива. |
| F021 | normalize_phone | трансформация | Нормализация телефона в формате E.164. |
| F022 | normalize_email | трансформация | Очистка email (trim, lowercase). |
| F023 | parse_date | трансформация | Преобразование даты в ISO формат. |
| F024 | format_date | трансформация | Форматирование ISO даты в заданный шаблон. |
| F025 | trim_whitespace | трансформация | Удаление пробелов по краям строки. |
| F026 | to_uppercase | трансформация | Перевод строки в верхний регистр. |
| F027 | to_lowercase | трансформация | Перевод строки в нижний регистр. |
| F028 | replace_regex | трансформация | Замена подстрок по регулярному выражению. |
| F029 | split_string | трансформация | Разделение строки по разделителю. |
| F030 | join_strings | трансформация | Склейка массива строк с разделителем. |
| F031 | map_values | трансформация | Преобразование значений по правилу. |
| F032 | filter_fields | трансформация | Отбор полей по списку разрешенных. |
| F033 | merge_records | трансформация | Объединение полей нескольких записей. |
| F034 | flatten_json | трансформация | Преобразование JSON в плоские ключи. |
| F035 | unflatten_json | трансформация | Восстановление вложенного JSON из плоских ключей. |
| F036 | deduplicate_records | трансформация | Удаление дублей по набору ключей. |
| F037 | convert_units | трансформация | Конвертация единиц измерения. |
| F038 | cast_types | трансформация | Приведение типов полей к целевым. |
| F039 | reorder_columns | трансформация | Перестановка колонок в заданном порядке. |
| F040 | calculate_hash | трансформация | Вычисление хэша записи для сверки. |
| F041 | create_table | хранение | Создание таблицы в базе данных. |
| F042 | insert_rows | хранение | Вставка строк в таблицу. |
| F043 | update_rows | хранение | Обновление строк по условию. |
| F044 | delete_rows | хранение | Удаление строк по условию. |
| F045 | query_sql | хранение | Выполнение SQL запроса и возврат результата. |
| F046 | create_index | хранение | Создание индекса для ускорения поиска. |
| F047 | drop_index | хранение | Удаление индекса таблицы. |
| F048 | upsert_rows | хранение | Вставка или обновление строк по ключу. |
| F049 | begin_transaction | хранение | Открытие транзакции в базе данных. |
| F050 | commit_transaction | хранение | Фиксация транзакции в базе данных. |
| F051 | rollback_transaction | хранение | Откат транзакции при ошибке. |
| F052 | backup_dataset | хранение | Создание резервной копии набора данных. |
| F053 | restore_dataset | хранение | Восстановление набора данных из бэкапа. |
| F054 | export_s3 | хранение | Экспорт данных в объектное хранилище S3. |
| F055 | import_s3 | хранение | Импорт данных из объекта S3. |
| F056 | create_bucket | хранение | Создание бакета в объектном хранилище. |
| F057 | delete_bucket | хранение | Удаление бакета в объектном хранилище. |
| F058 | list_objects | хранение | Получение списка объектов в бакете. |
| F059 | get_object_metadata | хранение | Чтение метаданных объекта хранения. |
| F060 | set_object_metadata | хранение | Обновление метаданных объекта хранения. |
| F061 | http_get | коммуникации | Выполнение HTTP GET запроса. |
| F062 | http_post | коммуникации | Выполнение HTTP POST запроса. |
| F063 | http_put | коммуникации | Выполнение HTTP PUT запроса. |
| F064 | http_delete | коммуникации | Выполнение HTTP DELETE запроса. |
| F065 | http_request | коммуникации | Универсальный HTTP запрос по методу. |
| F066 | call_webhook | коммуникации | Вызов внешнего вебхука с payload. |
| F067 | send_email | коммуникации | Отправка электронного письма. |
| F068 | send_sms | коммуникации | Отправка SMS сообщения. |
| F069 | send_push | коммуникации | Отправка push уведомления. |
| F070 | publish_queue | коммуникации | Публикация сообщения в очередь. |
| F071 | consume_queue | коммуникации | Чтение сообщений из очереди. |
| F072 | publish_topic | коммуникации | Публикация события в topic. |
| F073 | subscribe_topic | коммуникации | Подписка на события topic. |
| F074 | open_ws | коммуникации | Открытие WebSocket соединения. |
| F075 | close_ws | коммуникации | Закрытие WebSocket соединения. |
| F076 | send_ws_message | коммуникации | Отправка сообщения по WebSocket. |
| F077 | fetch_oauth_token | коммуникации | Получение OAuth токена по креденшелам. |
| F078 | refresh_oauth_token | коммуникации | Обновление OAuth токена по refresh token. |
| F079 | upload_sftp | коммуникации | Загрузка файла на SFTP сервер. |
| F080 | download_sftp | коммуникации | Скачивание файла с SFTP сервера. |
| F081 | calculate_sum | аналитика | Расчет суммы по числовому полю. |
| F082 | calculate_avg | аналитика | Расчет среднего значения по полю. |
| F083 | calculate_median | аналитика | Расчет медианы по полю. |
| F084 | calculate_percentile | аналитика | Расчет перцентиля по полю. |
| F085 | calculate_stddev | аналитика | Расчет стандартного отклонения. |
| F086 | calculate_zscore | аналитика | Вычисление Z-оценки значения. |
| F087 | detect_outliers | аналитика | Поиск выбросов по правилу. |
| F088 | compute_correlation | аналитика | Расчет корреляции между полями. |
| F089 | compute_covariance | аналитика | Расчет ковариации между полями. |
| F090 | fit_linear_regression | аналитика | Обучение линейной регрессии. |
| F091 | predict_linear_regression | аналитика | Прогноз по линейной регрессии. |
| F092 | cluster_kmeans | аналитика | Кластеризация k-means. |
| F093 | classify_text | аналитика | Классификация текста по меткам. |
| F094 | extract_entities | аналитика | Извлечение сущностей из текста. |
| F095 | detect_language | аналитика | Определение языка текста. |
| F096 | sentiment_analysis | аналитика | Анализ тональности текста. |
| F097 | recommend_items | аналитика | Генерация рекомендаций для пользователя. |
| F098 | compute_retention | аналитика | Расчет удержания пользователей по когорте. |
| F099 | cohort_analysis | аналитика | Анализ поведения когорт по периоду. |
| F100 | funnel_analysis | аналитика | Анализ воронки действий пользователя. |

## 6. Полные паспорта (12 функций)

### read_csv
- **Входы:** `path` (string, обяз.), `delimiter` (string, опц.), `encoding` (string, опц.).
- **Выходы:** `rows` (array), `columns` (array), `row_count` (integer).
- **Ошибки:** `FILE_NOT_FOUND`, `INVALID_ENCODING`, `PARSE_ERROR`.
- **Ограничения:** размер файла до 2 ГБ, до 1 млн строк за вызов.

### write_json
- **Входы:** `data` (object/array, обяз.), `path` (string, обяз.), `pretty` (boolean, опц.).
- **Выходы:** `status` (string), `bytes_written` (integer).
- **Ошибки:** `INVALID_PATH`, `PERMISSION_DENIED`, `SERIALIZATION_ERROR`.
- **Ограничения:** размер результата до 2 ГБ.

### export_pdf_report
- **Входы:** `template_id` (string, обяз.), `params` (object, опц.), `path` (string, обяз.).
- **Выходы:** `status` (string), `path` (string), `pages` (integer).
- **Ошибки:** `TEMPLATE_NOT_FOUND`, `RENDER_ERROR`, `WRITE_FAILED`.
- **Ограничения:** до 200 страниц за отчет.

### normalize_phone
- **Входы:** `phone` (string, обяз.), `default_country` (string, опц.).
- **Выходы:** `normalized` (string), `is_valid` (boolean).
- **Ошибки:** `VALIDATION_ERROR`, `UNSUPPORTED_COUNTRY`.
- **Ограничения:** длина входа до 64 символов.

### flatten_json
- **Входы:** `data` (object, обяз.), `separator` (string, опц.).
- **Выходы:** `flat` (object), `key_count` (integer).
- **Ошибки:** `INVALID_INPUT`, `CYCLE_DETECTED`.
- **Ограничения:** глубина вложенности до 64 уровней.

### upsert_rows
- **Входы:** `table` (string, обяз.), `rows` (array, обяз.), `keys` (array, обяз.).
- **Выходы:** `inserted` (integer), `updated` (integer).
- **Ошибки:** `TABLE_NOT_FOUND`, `CONSTRAINT_VIOLATION`, `DB_TIMEOUT`.
- **Ограничения:** до 10 000 строк за вызов.

### query_sql
- **Входы:** `sql` (string, обяз.), `params` (array/object, опц.).
- **Выходы:** `rows` (array), `row_count` (integer), `elapsed_ms` (integer).
- **Ошибки:** `SYNTAX_ERROR`, `PERMISSION_DENIED`, `DB_TIMEOUT`.
- **Ограничения:** время выполнения до 30 сек, результат до 100 000 строк.

### backup_dataset
- **Входы:** `dataset` (string, обяз.), `destination` (string, опц.).
- **Выходы:** `backup_id` (string), `status` (string).
- **Ошибки:** `DATASET_NOT_FOUND`, `IO_ERROR`, `QUOTA_EXCEEDED`.
- **Ограничения:** до 5 бэкапов на набор.

### http_request
- **Входы:** `method` (string, обяз.), `url` (string, обяз.), `headers` (object, опц.), `body` (object/string, опц.), `timeout_ms` (integer, опц.).
- **Выходы:** `status` (integer), `headers` (object), `body` (string/object).
- **Ошибки:** `INVALID_URL`, `TIMEOUT`, `NETWORK_ERROR`.
- **Ограничения:** размер тела до 10 МБ, таймаут до 30 сек.

### send_email
- **Входы:** `to` (array, обяз.), `subject` (string, обяз.), `body` (string, обяз.), `cc` (array, опц.).
- **Выходы:** `message_id` (string), `status` (string).
- **Ошибки:** `INVALID_ADDRESS`, `SMTP_ERROR`, `RATE_LIMITED`.
- **Ограничения:** до 50 получателей за письмо.

### calculate_percentile
- **Входы:** `values` (array<number>, обяз.), `p` (number, обяз.).
- **Выходы:** `value` (number), `method` (string).
- **Ошибки:** `INVALID_PERCENTILE`, `EMPTY_INPUT`.
- **Ограничения:** до 1 млн значений.

### cluster_kmeans
- **Входы:** `vectors` (array<array<number>>, обяз.), `k` (integer, обяз.), `max_iter` (integer, опц.).
- **Выходы:** `centroids` (array), `labels` (array).
- **Ошибки:** `INVALID_K`, `EMPTY_INPUT`, `CONVERGENCE_FAILED`.
- **Ограничения:** до 100 000 точек, `k` до 100.

## 7. Проверка дублей и стандартизация формулировок
- Дубли в списке из 100 функций не выявлены, идентификаторы уникальны и упорядочены.
- Формулировки описаний приведены к единому стилю: глагол действия + объект.
