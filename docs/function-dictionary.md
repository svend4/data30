# Function Dictionary (MVP)

## 1) Краткое введение
Function Dictionary — единый язык описания атомарных действий. Он нужен, чтобы:
- унифицировать функции из разных приложений;
- строить сценарии и макросы на общих терминах;
- обеспечить поиск, рейтинг и совместимость.

## 2) Принципы использования
1. Названия функций — в едином стиле: глагол + объект (например, CreateLead, SendEmail).
2. Описание функции должно быть атомарным и не включать несколько действий.
3. Категория выбирается по основному эффекту функции (например, SendEmail → OUT).
4. При пересечении функций выбирается более общая, а специфические варианты оформляются как отдельные.

## 3) MVP-словарь (100 функций)

**Категории:**
- **IN** — ввод/получение данных
- **OUT** — вывод/отправка
- **TR** — трансформация
- **ST** — хранение
- **AN** — аналитика
- **AC** — управление доступом
- **OR** — оркестрация

| ID | Функция | Категория | Краткое описание |
|---|---|---|---|
| F001 | GetHTTP | IN | Получить данные по HTTP запросу |
| F002 | ReceiveWebhook | IN | Принять входящий webhook |
| F003 | ReadFile | IN | Прочитать файл |
| F004 | ParseCSV | TR | Парсинг CSV в структуру |
| F005 | ParseJSON | TR | Парсинг JSON |
| F006 | ParseXML | TR | Парсинг XML |
| F007 | ExtractText | TR | Извлечь текст из документа |
| F008 | OCRImage | TR | Распознавание текста на изображении |
| F009 | ValidateEmail | TR | Проверка email |
| F010 | ValidatePhone | TR | Проверка телефона |
| F011 | NormalizeData | TR | Нормализация данных |
| F012 | MapFields | TR | Сопоставление полей |
| F013 | MergeData | TR | Объединить записи |
| F014 | SplitData | TR | Разделить набор данных |
| F015 | Deduplicate | TR | Удалить дубликаты |
| F016 | EncryptData | TR | Шифрование данных |
| F017 | DecryptData | TR | Расшифровка данных |
| F018 | GenerateUUID | TR | Сгенерировать UUID |
| F019 | ConvertFormat | TR | Конвертация формата |
| F020 | FilterData | TR | Фильтрация |
| F021 | SortData | TR | Сортировка |
| F022 | AggregateData | AN | Агрегация |
| F023 | CalculateMetric | AN | Расчет метрики |
| F024 | GenerateReport | AN | Генерация отчета |
| F025 | LogEvent | ST | Записать событие |
| F026 | WriteFile | ST | Записать файл |
| F027 | UploadFile | OUT | Загрузить файл |
| F028 | DownloadFile | IN | Скачать файл |
| F029 | SaveToDB | ST | Записать в базу данных |
| F030 | ReadFromDB | IN | Читать из БД |
| F031 | UpdateRecord | ST | Обновить запись |
| F032 | DeleteRecord | ST | Удалить запись |
| F033 | CreateRow | ST | Создать строку |
| F034 | UpdateRow | ST | Обновить строку |
| F035 | DeleteRow | ST | Удалить строку |
| F036 | SearchRecords | IN | Поиск записей |
| F037 | SendEmail | OUT | Отправить email |
| F038 | SendSMS | OUT | Отправить SMS |
| F039 | SendPush | OUT | Отправить push |
| F040 | SendMessage | OUT | Отправить сообщение |
| F041 | CreateTicket | ST | Создать тикет |
| F042 | UpdateTicket | ST | Обновить тикет |
| F043 | CloseTicket | ST | Закрыть тикет |
| F044 | CreateLead | ST | Создать лид |
| F045 | UpdateLead | ST | Обновить лид |
| F046 | CreateDeal | ST | Создать сделку |
| F047 | UpdateDeal | ST | Обновить сделку |
| F048 | CreateContact | ST | Создать контакт |
| F049 | UpdateContact | ST | Обновить контакт |
| F050 | CreateTask | ST | Создать задачу |
| F051 | UpdateTask | ST | Обновить задачу |
| F052 | CompleteTask | ST | Завершить задачу |
| F053 | CreateEvent | ST | Создать событие |
| F054 | UpdateEvent | ST | Обновить событие |
| F055 | CreateCalendar | ST | Создать календарь |
| F056 | AddCalendarEvent | ST | Добавить событие в календарь |
| F057 | RemoveCalendarEvent | ST | Удалить событие |
| F058 | CreateUser | AC | Создать пользователя |
| F059 | UpdateUser | AC | Обновить пользователя |
| F060 | DeleteUser | AC | Удалить пользователя |
| F061 | AssignRole | AC | Назначить роль |
| F062 | RevokeRole | AC | Отозвать роль |
| F063 | Authenticate | AC | Аутентификация |
| F064 | Authorize | AC | Авторизация |
| F065 | CreateDocument | ST | Создать документ |
| F066 | UpdateDocument | ST | Обновить документ |
| F067 | SignDocument | ST | Подписать документ |
| F068 | ArchiveDocument | ST | Архивировать документ |
| F069 | GeneratePDF | TR | Сформировать PDF |
| F070 | GenerateTemplate | TR | Сгенерировать шаблон |
| F071 | RenderHTML | TR | Рендер HTML |
| F072 | TranslateText | TR | Перевод текста |
| F073 | SummarizeText | AN | Суммаризация текста |
| F074 | ClassifyText | AN | Классификация текста |
| F075 | DetectLanguage | AN | Определение языка |
| F076 | ExtractEntities | AN | Извлечение сущностей |
| F077 | AnalyzeSentiment | AN | Анализ тональности |
| F078 | GenerateImage | TR | Генерация изображения |
| F079 | ResizeImage | TR | Изменение размера |
| F080 | CompressImage | TR | Сжатие изображения |
| F081 | CreateInvoice | ST | Создать счет |
| F082 | UpdateInvoice | ST | Обновить счет |
| F083 | PayInvoice | OUT | Оплатить счет |
| F084 | CreatePayment | ST | Создать платеж |
| F085 | RefundPayment | OUT | Возврат платежа |
| F086 | CreateSubscription | ST | Создать подписку |
| F087 | CancelSubscription | ST | Отменить подписку |
| F088 | GetAnalytics | AN | Получить аналитику |
| F089 | CreateDashboard | AN | Создать дашборд |
| F090 | UpdateDashboard | AN | Обновить дашборд |
| F091 | ScheduleTask | OR | Планирование выполнения |
| F092 | RetryTask | OR | Повтор выполнения |
| F093 | BranchFlow | OR | Ветвление сценария |
| F094 | JoinFlow | OR | Слияние ветвей |
| F095 | Throttle | OR | Ограничение частоты |
| F096 | QueueTask | OR | Поместить задачу в очередь |
| F097 | DequeueTask | OR | Извлечь задачу |
| F098 | MonitorStatus | OR | Мониторинг статуса |
| F099 | AlertOnFailure | OR | Уведомление о сбое |
| F100 | LogAudit | ST | Запись аудита |

## 4) Расширенные паспорта функций (12 шт.)

### F002 — ReceiveWebhook
- **Категория:** IN
- **Вход:** HTTP-запрос, заголовки, payload
- **Выход:** status, parsed_body
- **Ошибки:** invalid_signature, invalid_payload
- **Ограничения:** rate limit
- **Пример:** прием формы сайта

### F004 — ParseCSV
- **Категория:** TR
- **Вход:** CSV-файл, delimiter
- **Выход:** array<row>
- **Ошибки:** invalid_csv
- **Ограничения:** max_rows
- **Пример:** импорт контактов

### F009 — ValidateEmail
- **Категория:** TR
- **Вход:** email
- **Выход:** is_valid, reason
- **Ошибки:** malformed_input
- **Ограничения:** none
- **Пример:** проверка заявки

### F012 — MapFields
- **Категория:** TR
- **Вход:** source_schema, target_schema, mapping
- **Выход:** mapped_object
- **Ошибки:** missing_field
- **Ограничения:** mapping depth
- **Пример:** CRM → рассылка

### F029 — SaveToDB
- **Категория:** ST
- **Вход:** record, table
- **Выход:** record_id
- **Ошибки:** db_error
- **Ограничения:** transaction limits
- **Пример:** запись лида

### F036 — SearchRecords
- **Категория:** IN
- **Вход:** query, filters
- **Выход:** records
- **Ошибки:** invalid_query
- **Ограничения:** max_results
- **Пример:** поиск клиента

### F037 — SendEmail
- **Категория:** OUT
- **Вход:** to, subject, body
- **Выход:** status, message_id
- **Ошибки:** auth_failed, invalid_email
- **Ограничения:** rate limit
- **Пример:** отправка уведомления

### F044 — CreateLead
- **Категория:** ST
- **Вход:** lead_data
- **Выход:** lead_id
- **Ошибки:** validation_error
- **Ограничения:** required fields
- **Пример:** регистрация лида

### F065 — CreateDocument
- **Категория:** ST
- **Вход:** template_id, data
- **Выход:** document_id
- **Ошибки:** template_missing
- **Ограничения:** size limit
- **Пример:** договор

### F067 — SignDocument
- **Категория:** ST
- **Вход:** document_id, signer
- **Выход:** signed_document_id
- **Ошибки:** invalid_signature
- **Ограничения:** certificate validity
- **Пример:** электронная подпись

### F073 — SummarizeText
- **Категория:** AN
- **Вход:** text
- **Выход:** summary
- **Ошибки:** input_too_large
- **Ограничения:** max_tokens
- **Пример:** краткий отчет

### F091 — ScheduleTask
- **Категория:** OR
- **Вход:** task_id, schedule
- **Выход:** schedule_id
- **Ошибки:** invalid_schedule
- **Ограничения:** timezone support
- **Пример:** запуск рассылки

## 5) Правила расширения словаря
1. Функция добавляется, если ее нельзя корректно описать существующей комбинацией функций.
2. Для каждой новой функции требуется краткое описание и указание категории.
3. Если функция предполагает вход/выход, следует описать входы/выходы явно.
4. При сомнении добавляется примечание в формате комментария к паспорту функции.
