from .base import Base
from .utils import validate_amount


class Transfer(Base):
    def initiate_transfer(self, amount:float, recipient:str, reason:str=None, currency:str=None, reference:str=None):
        endpoint = '/transfer'

        amount = validate_amount(amount) * 100

        data = {
            'source':"balance",
            'amount':amount,
            'recipient':recipient
        }

        if reason is not None:
            data['reason'] = reason
        if currency is not None:
            data['currency'] = currency
        if reference is not None:
            data['reference'] = reference

        return self.handle_request("POST", endpoint=endpoint, data=data)

    def finalize_transfer(self, transfer_code:str, otp:str):
        endpoint = '/transfer/finalize_transfer'

        data = {
            'transfer_code':transfer_code,
            'otp':otp
        }

        return self.handle_request("POST", endpoint=endpoint, data=data)

    def initiate_bulk_transfer(self, transfers:list):
        endpoint = '/transfer/bulk'

        data = {
            'source':"balance",
            'transfers':transfers
        }

        return self.handle_request("POST", endpoint=endpoint, data=data)
    
    def list_transfers(self):
        endpoint = '/transfer'

        return self.handle_request("GET", endpoint=endpoint)

    def fetch_transfer(self, id_or_code:str):
        endpoint = f'/transfer/{id_or_code}'

        return self.handle_request("GET", endpoint=endpoint)

    def verify_transfer(self, reference:str):
        endpoint = f'/transfer/verify/{reference}'

        return self.handle_request("GET", endpoint=endpoint)