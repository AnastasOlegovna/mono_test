"""This module handles webhooks for the application."""
from flask import Flask, request
import hashlib
import base64
import ecdsa
import os
from os.path import join, dirname
from dotenv import load_dotenv
import unittest

app = Flask(__name__)


def get_from_env(key):
    """
    Return key.

    :param key: required name of key
    :type key: str

    :return: value of key_name
    :rtype: str

    """
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)  # GET TOKEN


class TestGetFromEnv(unittest.TestCase):
    """Unit test class for testing the get_from_env function."""

    def setUp(self):
        """Set up the test environment. This method is called before each test."""
        self.key = 'TEST_KEY'
        self.value = 'TEST_VALUE'
        os.environ[self.key] = self.value

    def test_get_from_env(self):
        """Test the get_from_env function with a key that exists in the environment."""
        self.assertEqual(get_from_env(self.key), self.value)

    def tearDown(self):
        """Clean up the test environment. This method is called after each test."""
        del os.environ[self.key]


# Prod
API_SECRET_KEY = get_from_env('API_KEY')


# Test
# API_SECRET_KEY = get_from_env('API_TEST')


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

    """
    # Your function code here
    pub_key_bytes = base64.b64decode(API_SECRET_KEY)
    signature_bytes = base64.b64decode(hmac_header)
    pub_key = ecdsa.VerifyingKey.from_pem(pub_key_bytes.decode())
    ok = pub_key.verify(signature_bytes, data, sigdecode=ecdsa.util.sigdecode_der, hashfunc=hashlib.sha256)

    return ok


@app.route('/', methods=['POST'])
def handle_webhook():
    """
    Handle incoming webhooks, verify their authenticity, and print the response.

    This function retrieves the raw data from the incoming webhook request and the 'X-Sign' from the headers.
    It then verifies the webhook using the 'verify_webhook' function. If the webhook is verified, it prints
    "verified" and the JSON response from the request. If the webhook is not verified, it prints "not verified".

    :return: A dictionary with a single key-value pair, where the key is 'ok' and the value is True.
    :rtype: dict
    """
    # Get raw body
    data = request.get_data()
    # print(f'Raw data:{data}')
    x_sign = request.headers.get('X-Sign')
    ok = verify_webhook(data, x_sign)
    # print(f'data: {data}')
    # print(f'hah: {x_sign}')

    if ok:
        print("verified")
        response = request.json
        print(f'Update:{response}')
    else:
        print("not verified")
    return {"ok": True}


if __name__ == "__main__":
    # Set webhook for the bot
    unittest.main(exit=False)
    app.run(host='localhost', port=8013)
