from .base import Base
from pydantic import EmailStr

class Customer(Base):
    def create_customer(self, email:EmailStr, first_name:str, last_name:str, phone:str=None, metadata:dict=None):
        endpoint = '/customer'

        data = {
            'email':email,
            'first_name':first_name,
            'last_name':last_name
        }

        if phone is not None:
            data['phone'] = phone
        if metadata is not None:
            data['metadata'] = metadata
        

        return self.handle_request("POST", endpoint=endpoint, data=data)

    def list_customer(self):
        endpoint = '/customer'

        return self.handle_request("GET", endpoint=endpoint)

    def fetch_customer(self, email_or_code:str):
        endpoint = f'/customer/{email_or_code}'

        return self.handle_request("GET", endpoint=endpoint)

    def update_customer(self, code:str, first_name:str, last_name:str, phone:str=None, metadata:dict=None):
        endpoint = f'/customer/{code}'

        data = {
            'first_name':first_name,
            'last_name':last_name
        }

        if phone:
            data['phone'] = phone
        if metadata:
            data['metadata'] = metadata

        return self.handle_request("PUT", endpoint=endpoint, data=data)

    def validate_customer(self, code:str, first_name:str, last_name:str, identification_type:str, value:str, country:str, bvn:str, bank_code:str, account_number:str, middle_name:str=None):
        endpoint = f'/customer/{code}/identification'

        data = {
            'first_name':first_name,
            'last_name':last_name,
            'identification_type':identification_type,
            'value':value,
            'country':country,
            'bvn':bvn,
            'bank_code':bank_code,
            'account_number':account_number
        }

        if middle_name is not None:
            data['middle_name'] = middle_name

        return self.handle_request("POST", endpoint=endpoint, data=data)

    def whitelist_customer(self, code:str):
        endpoint = f'/customer/set_risk_action'

        data = {
            'customer':code,
            'risk_action':'allow'
        }

        return self.handle_request("POST", endpoint=endpoint, data=data)

    def blacklist_customer(self, code:str):
        endpoint = f'/customer/set_risk_action'

        data = {
            'customer':code,
            'risk_action':'deny'
        }

        return self.handle_request("POST", endpoint=endpoint, data=data)

    def deactivate_customer(self, authorization_code:str):
        endpoint = f'/customer/deactivate_authorization'

        data = {
            'authorization_code':authorization_code
        }

        return self.handle_request("POST", endpoint=endpoint, data=data)
