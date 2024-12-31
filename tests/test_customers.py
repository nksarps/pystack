import unittest
from decouple import config
from pystack import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.test_key = config('TEST_KEY')
        self.customer = Customer(self.test_key)


    def test_create_customer(self):
        email = 'mail@example.com'
        first_name = 'Jane'
        last_name = 'Doe'


        response = self.customer.create_customer(email=email, first_name=first_name, last_name=last_name)

        data = {
            'email': 'mail@example.com',    
            'first_name': 'Jane',
            'last_name': 'Doe',
        }

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Customer created')
        self.assertEqual(response['data']['email'], data['email'])
        self.assertEqual(response['data']['first_name'], data['first_name'])
        self.assertEqual(response['data']['last_name'], data['last_name'])
    
    def test_list_customer(self):
        response = self.customer.list_customer()

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Customers retrieved')
        self.assertIsInstance(response['data'], list)

    def test_fetch_customer(self):
        email_or_code = 'mail@example.com'

        response = self.customer.fetch_customer(email_or_code)
        
        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Customer retrieved')
        self.assertEqual(response['data']['email'], email_or_code)
        self.assertIsInstance(response['data'], dict)

    def test_update_customer(self):
        code = 'CUS_v139w7vtm31u4yy'
        first_name = 'Jane'
        last_name = 'Doe'

        response = self.customer.update_customer(code, first_name, last_name)

        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
        }

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Customer updated')
        self.assertEqual(response['data']['first_name'], data['first_name'])
        self.assertEqual(response['data']['last_name'], data['last_name'])
    
    # URL Not Found
    def test_validate_customer(self):
        code = 'CUS_v139w7vtm31u4yy'
        first_name = 'Jane'
        last_name = 'Doe'
        identification_type = 'bank_account'
        value = '12345678901'
        country = 'NG'
        bvn = '12345678901'
        bank_code = '044'
        account_number = '1234567890'

        response = self.customer.validate_customer(code, first_name, last_name, identification_type, value, country, bvn, bank_code, account_number)

        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'identification_type': 'BVN',
            'value': '12345678901',
            'country': 'GH',
            'bvn': '12345678901',
            'bank_code': '044',
            'account_number': '1234567890'
        }

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Customer Identification in progress')

    def test_whitelist_customer(self):
        code = 'CUS_v139w7vtm31u4yy'
        response = self.customer.blacklist_customer(code)

        data = {
            'code': 'CUS_v139w7vtm31u4yy',
        }

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Customer updated')

    def test_blacklist_customer(self):
        code = 'CUS_v139w7vtm31u4yy'
        response = self.customer.blacklist_customer(code)

        data = {
            'code': 'CUS_v139w7vtm31u4yy',
        }

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Customer updated')

    # URL Not Found
    def test_deactivate_customer(self):
        authorization_code = 'AUTH_72btv547'

        response = self.customer.deactivate_customer(authorization_code)

        data = {
            'authorization_code': 'AUTH_72btv547',
        }

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Authorization has been deactivated')

if __name__ == '__main__':
    unittest.main()