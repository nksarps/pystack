from .base import Base
from .utils import validate_amount

class Plan(Base):
    def create_plan(self, name:str, amount:float, interval:str, description:str=None, currency:str=None):
        endpoint = '/plan'

        amount = validate_amount(amount) * 100

        data = {
            'name':name,
            'amount':str(amount),
            'interval':interval
        }

        if description is not None:
            data['description'] = description
        if currency is not None:
            data['currency'] = currency
        
        return self.handle_request("POST", endpoint=endpoint, data=data)

    def list_plans(self):
        endpoint = '/plan'

        return self.handle_request("GET", endpoint=endpoint)

    def fetch_plan(self, id_or_code:str):
        endpoint = f'/plan/{id_or_code}'

        return self.handle_request("GET", endpoint=endpoint)

    def update_plan(self, id_or_code:str, name:str, amount:float, interval:str, description:str=None, currency:str=None):
        endpoint = f'/plan/{id_or_code}'

        amount = validate_amount(amount) * 100

        data = {
            'name':name,
            'amount':str(amount),
            'interval':interval
        }

        if description is not None:
            data['description'] = description
        if currency is not None:
            data['currency'] = currency

        return self.handle_request("PUT", endpoint=endpoint)
