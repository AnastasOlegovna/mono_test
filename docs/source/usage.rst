Usage
=====

.. _installation:

Installation
------------

1. To use module, first install requirements.txt:

.. code-block:: console

   (.venv) docs$ pip install -r requirements.txt

2. Create your own reverse proxy to receive webhooks directly in the app in 'localhost' and port 8013

For test, I use `Ngrok <https://ngrok.com/docs/getting-started>`_

3. Create .env file

.. note::

    inside file write API_KEY=<YOUR_API_KEY>

    Don't forget set your address in invoice ``param: "webHookUrl": "your_address"``

    If you have 2 and more shops, use ``param: "reference": "shop_number"``

Use
---

Get your API key,
you can use the ``get_from_env(key)`` function

.. autofunction:: webhook_prod.get_from_env

You can see small test ``get_from_env(key)`` function

>>> import webhook_prod
>>> webhook_prod.get_from_env("Test")
'Test'

To try verify your webhook,
you can use the ``verify_webhook(data, hmac_header)`` function

.. autofunction:: webhook_prod.verify_webhook

For listening all webhook, you can use ``handle_webhook()`` function

.. autofunction:: webhook_prod.handle_webhook