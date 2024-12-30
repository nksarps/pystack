import json, requests
from .errors import MissingSecretKeyError, InvalidMethodError
from requests.exceptions import RequestException

class Base(object):
    BASE_URL = "https://api.paystack.co"

    def __init__(self, secret_key) -> None:
        if not secret_key:
            raise MissingSecretKeyError("A secret key is required.")
        self.secret_key = secret_key


    def headers(self):
        return {
            "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json"
        }

    def handle_request(self, method, endpoint, data=None, params=None):
        methods = {
            'POST':requests.post,
            'GET':requests.get,
            'PUT':requests.put,
            'DELETE':requests.delete
        }

        request = methods.get(method.upper())

        if not request:
            raise InvalidMethodError(f"Request method '{method}' not recognised")
        
        url = f'{self.BASE_URL}{endpoint}'
        try:
            response = request(url, headers=self.headers(), json=data, params=params)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f'error: {str(e)}')