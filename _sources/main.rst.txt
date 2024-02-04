Створення рахунку
=================

Створення рахунку для оплати

HEADER PARAMETERS
-----------------

.. list-table::
   :header-rows: 1

   * - **HEADER PARAMETERS**
     - **TYPE**
     - **DESCRIPTION**
   * - X-Token
     - | string
     - Токен з особистого кабінету https://web.monobank.ua/ або тестовий токен з https://api.monobank.ua/
   * - X-Cms
     - | string
     - Назва CMS, якщо ви розробляєте платіжний модуль для CMS
   * - X-Cms-Version
     - | string
     - Версія CMS, якщо ви розробляєте платіжний модуль для CMS

.. container:: toggle, toggle-hidden

    .. admonition:: POST request!

        This is a POST request to `api/merchant/invoice/create`.


REQUEST BODY SCHEMA: application/json
--------------------------------------

amount
    required
    integer <int64>
    Сума оплати у мінімальних одиницях (копійки для гривні)

ccy
    integer <int32>
    ISO 4217 код валюти, за замовчуванням 980 (гривня)

merchantPaymInfo
    object (MerchantPaymInfoItem)
    Інформаційні дані замовлення, яке буде оплачуватсь. Обовʼязково вказувати при активній звʼязці з ПРРО (звʼязка створюється у веб-кабінеті https://web.monobank.ua)

redirectUrl
    string
    Адреса для повернення (GET) - на цю адресу буде переадресовано користувача після завершення оплати (у разі успіху або помилки)

webHookUrl
    string
    Адреса для CallBack (POST) – на цю адресу буде надіслано дані про стан платежу при кожній зміні статусу. Зміст тіла запиту ідентичний відповіді запиту “Статус рахунку”. Гарантії доставки повідомлень одне за одним не надається. Тобто, може бути ситуація, коли вебхук про успішну оплату (status=success) прийде пізніше за вебхук про обробку цієї оплати (status=processing). Краще орієнтуватись на поле modifiedDate при аналізі поточного статусу рахунку. Вебухк із більшим modifiedDate буде актуальним

validity
    integer <int64>
    Строк дії в секундах, за замовчуванням рахунок перестає бути дійсним через 24 години

paymentType
    string
    Default: "debit"
    Enum: "debit" "hold"
    Тип операції. Для значення hold термін складає 9 днів. Якщо через 9 днів холд не буде фіналізовано — він скасовується

qrId
    string
    Ідентифікатор QR-каси для встановлення суми оплати на існуючих QR-кас

code
    string
    Код терміналу субмерчанта, з апі "Список субмерчантів". Доступний обмеженому колу мерчантів, які точно знають, що їм це потрібно

saveCardData
    object
    Дані для збереження (токенізації) картки. Для підключення функції, зверніться, будь ласка, в підтримку monobank. Токенізація недоступна за замовчуванням

Request Samples
---------------

.. code-block:: json

   {
       "amount": 100,
       "ccy": 980,
       "merchantPayload": {
           "id": "1234567890",
           "description": "Опис замовлення",
           "amount": 100,
           "ccy": 980
       },
       "redirectUrl": "https://example.com",
       "webHookUrl": "https://example.com",
       "validity": 86400,
       "paymentType": "debit",
       "qrId": "1234567890",
       "code": "1234567890",
       "saveCardData": {
           "returnUrl": "https://example.com"
       }
   }
