from .base import Base
from .errors import InvalidDataError
from .utils import validate_amount
from pydantic import EmailStr


class Transaction(Base):
    def initialize_transaction(self, amount:float, email:EmailStr, metadata:dict=None):
        endpoint = '/transaction/initialize'

        amount = validate_amount(amount) * 100

        data = {
            "email":email,
            "amount":str(amount)
        }

        # Add metadata is provided
        if metadata:
            data['metadata'] = metadata

        return self.handle_request("POST", endpoint=endpoint, data=data)

    def verify_transaction(self, reference:str):
        endpoint = f'/transaction/verify/{reference}'

        return self.handle_request("GET", endpoint=endpoint)

    def list_transaction(self):
        endpoint = '/transaction'

        return self.handle_request("GET", endpoint=endpoint)

    def fetch_transaction(self, id:int):
        endpoint = f'/transaction/{id}'

        return self.handle_request("GET", endpoint=endpoint)

    def charge_authorization(self, amount:float, email:EmailStr, authorization_code:str):
        endpoint = '/transaction/charge_authorization'

        amount = validate_amount(amount) * 100

        data = {
            "amount":str(amount),
            "email":email,
            "authorization_code":authorization_code
        }

        return self.handle_request("POST", endpoint=endpoint, data=data)

    def view_transaction_timeline(self, id_or_ref:str):
        endpoint = f'/transaction/timeline/{id_or_ref}'

        return self.handle_request("GET", endpoint=endpoint)

    def transaction_totals(self):
        endpoint = '/transaction/totals'

        return self.handle_request("GET", endpoint=endpoint)

    def export_transaction(self):
        endpoint = '/transaction/export'

        return self.handle_request("GET", endpoint=endpoint)

    def partial_debit(self, authorization_code:str, currency:str, amount:float, email:EmailStr):
        endpoint = '/transaction/partial_debit'

        amount = validate_amount(amount) * 100

        data = {
            "authorization_code": authorization_code, 
            "currency": currency, 
            "amount": str(amount),
            "email": email
        }

        self.handle_request("POST", endpoint=endpoint, data=data)