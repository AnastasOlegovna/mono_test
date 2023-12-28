"""This module handles webhooks for the application."""
from flask import Flask, request
import hashlib
import base64
import ecdsa
import os
from os.path import join, dirname
from dotenv import load_dotenv

app = Flask(__name__)


def get_from_env(key):
    """
    Return key

    :param key: required name of key
    :type key: str

    :return: value of key_name
    :rtype: str

    """
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)  # GET TOKEN


# Prod
API_SECRET_KEY = get_from_env('API_KEY')

# Test
# API_SECRET_KEY = get_from_env('API_TEST')


def verify_webhook(data, hmac_header):
    """
    Return ok

    :param data: required response in request.get_data()
    :type data: str or None
    :param hmac_header: required response in request.headers.get('X-Sign')
    :type hmac_header: list[str] or None
    :return: ok
    :rtype: str

    """
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
    if ok:
        print("verified")
        response = request.json
        print(f'Update:{response}')
    else:
        print("not verified")

    return {"ok": True}


if __name__ == "__main__":
    # Set webhook for the bot
    app.run(host='localhost', port=8013)
