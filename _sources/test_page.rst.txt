Компоненти (1)
==============

Іконки (піктограми)
-------------------

Використовуються в меню та інших компонентах

.. note::

   Використовуються в меню та інших компонентах

.. image:: example.gif
      :alt: Mono

.. image:: sorry.png
      :alt: Mono

Побажання

1. Змінити кольорову гаму (на мою думку вона не є ок)
2. Змінити компоненту статусів в карточці

.. admonition:: More
   :class: dropdown

   test
   my
   list

Варіант який можливо розглянути

.. |check| raw:: html

    <input checked=""  type="checkbox">

**Чек-лист**

|check| Один

|check| Два

|check| Три

************************************************************************************************************************

Required permission: ``ticket.agent`` or ``ticket.customer``

``GET``-Request sent: ``/api/v1/tickets``

Response:

.. raw:: html

    <details class="collapse-code">
    <summary>Click to expand</summary>

.. code-block:: json

   {
       "id": 1,
       "group_id": 1,
       "priority_id": 2,
       "state_id": 1,
       "organization_id": 1,
       "number": "22001",
       "title": "Welcome to Zammad!",
       "owner_id": null,
       "customer_id": null,
       "note": null,
       "first_response_at": null,
       "first_response_escalation_at": null
   }

.. raw:: html

    </details>

.. note::
    :class: dropdown

    - один
    - два
    - три

.. attention::

    Цитата


.. code-block:: python

    def verify_webhook(data, hmac_header):
        """
        Return ok.

        :param data: response from server Mono
        :param hmac_header: hash X-Sign from response
        :return: ok

        .. doctest:: :hide:

            >>> verify_webhook({
            ...   "invoiceId": "mockInvoiceId",
            ...   "status": "mockStatus",
            ...   "amount": 123,
            ...   "ccy": 456,
            ...   "createdDate": "2023-12-30T16:08:06Z",
            ...   "modifiedDate": "2023-12-30T16:08:06Z",
            ...   "reference": "mockReference"
            ... }, 'mockhash')  # replace with actual test data

            True  # expected output

        :return: ok
        """
        # Your function code here
        pub_key_bytes = base64.b64decode(API_SECRET_KEY)
        signature_bytes = base64.b64decode(hmac_header)
        pub_key = ecdsa.VerifyingKey.from_pem(pub_key_bytes.decode())
        ok = pub_key.verify(signature_bytes, data, sigdecode=ecdsa.util.sigdecode_der, hashfunc=hashlib.sha256)

        return ok

