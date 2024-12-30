import unittest
from decouple import config
from pystack.transactions import Transaction
from unittest.mock import patch, Mock


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.test_key = config('TEST_KEY')
        self.transaction = Transaction(self.test_key)
        self.expected_headers = {
            'Authorization': f'Bearer {self.test_key}',
            'Content-Type': 'application/json'
        }
        

    @patch('requests.post')
    def test_initialize_transaction(self, mock_post):
        mock_response = Mock()
        response_dict = {
            "status": True,
            "message": "Authorization URL created",
            "data": {
                "authorization_url": "https://checkout.paystack.com/3ni8kdavz62431k",
                "access_code": "3ni8kdavz62431k",
                "reference": "re4lyvq3s3"
            }
        }
        mock_response.json.return_value = response_dict

        mock_post.return_value = mock_response

        amount = 30
        email = 'example@gmail.com'
        metadata = {
            'order_id':'od57gd9'
        }

        response = self.transaction.initialize_transaction(amount, email, metadata)

        data = {
            'email':'example@gmail.com',
            'amount':'3000',
            'metadata':{
                'order_id':'od57gd9'
            }
        }

        mock_post.assert_called_with(
            f'https://api.paystack.co/transaction/initialize',
            headers=self.expected_headers,
            json=data,
            params=None
        )
        self.assertEqual(response, response_dict)

    @patch('requests.get')
    def test_verify_transaction(self, mock_get):
        mock_response = Mock()
        response_dict = {
            "status":True,
            "message":"Verification complete",
            "data":{
                "reference":"re4lyvq3s3"
            }
        }
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response

        reference = 're4lyvq3s3'
        response = self.transaction.verify_transaction(reference)
        
        mock_get.assert_called_with(
            f'https://api.paystack.co/transaction/verify/{reference}',
            headers=self.expected_headers,
            json=None,
            params=None
        )
        self.assertEqual(response, response_dict)

    @patch('requests.get')
    def test_list_transaction(self, mock_get):
        mock_response = Mock()
        response_dict = {
            "status": True,
            "message": "Transactions retrieved",
            'data': [
                {
                    "id": 4099260516,
                    "domain": "test",
                    "status": "success",
                    "reference": "re4lyvq3s3",
                    "amount": 40333,
                    "currency": "GHS"
                }
            ]
        }
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response

        response = self.transaction.list_transaction()

        mock_get.assert_called_with(
            f'https://api.paystack.co/transaction',
            headers=self.expected_headers,
            json=None,
            params=None
        )
        self.assertEqual(response, response_dict)

    @patch('requests.get')
    def test_fetch_transaction(self, mock_get):
        mock_response = Mock()
        response_dict = {
            "status": True,
            "message": "Transaction retrieved",
            'data': {
                "id": 4099260516,
                "domain": "test",
                "status": "success",
                "reference": "re4lyvq3s3",
                "amount": 40333,
                "currency": "GHS"
            }
        }
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response

        id = 4099260516
        response = self.transaction.fetch_transaction(id)

        mock_get.assert_called_with(
            f'https://api.paystack.co/transaction/{id}',
            headers=self.expected_headers,
            json=None,
            params=None
        )
        self.assertEqual(response, response_dict)

    @patch('requests.post')
    def test_charge_authorization(self, mock_post):
        mock_response = Mock()
        response_dict = {
            "status": True,
            "message": "Charge attempted",
            "data": {
                'amount': 3000,
                'currency': 'GHS',
                'status': 'success',
                'reference': '0m7frfnr47ezyxl',
            }
        }
        mock_response.json.return_value = response_dict

        mock_post.return_value = mock_response

        amount = 30
        email = 'mail@example.com'
        authorization_code = 'auth_code'

        response = self.transaction.charge_authorization(amount, email, authorization_code)

        data = {
            'amount':'3000',
            'email':'mail@example.com',
            'authorization_code':'auth_code'
        }

        mock_post.assert_called_with(
            f'https://api.paystack.co/transaction/charge_authorization',
            headers=self.expected_headers,
            json=data,
            params=None
        )

        self.assertEqual(response, response_dict)

    @patch('requests.get')
    def test_view_transaction_timeline(self, mock_get):
        mock_response = Mock()
        response_dict = {
            "status": True,
            "message": "Timeline retrieved",
            "data": {
                "start_time": 1724318098,
                "time_spent": 4,
                "attempts": 1,
                "errors": 0,
                "success": True,
            }
        }
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response

        id_or_ref = 're4lyvq3s3'
        response = self.transaction.view_transaction_timeline(id_or_ref)

        mock_get.assert_called_with(
            f'https://api.paystack.co/transaction/timeline/{id_or_ref}',
            headers=self.expected_headers,
            json=None,
            params=None
        )
        self.assertEqual(response, response_dict)

    @patch('requests.get')
    def test_transaction_totals(self, mock_get):
        mock_response = Mock()
        response_dict = {
            "status": True,
            "message": "Transaction totals",
            "data": {
                "total_volume": 3000,
                "total_transactions": 3,
                "pending_transfers": 0,
                "total_transfers": 0,
                "successful_transfers": 0,
                "failed_transfers": 0,
            }
        }
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response

        response = self.transaction.transaction_totals()

        mock_get.assert_called_with(
            f'https://api.paystack.co/transaction/totals',
            headers=self.expected_headers,
            json=None,
            params=None
        )
        self.assertEqual(response, response_dict)

    @patch('requests.get')
    def test_export_transaction(self, mock_get):
        mock_response = Mock()
        response_dict = {
            "status": True,
            "message": "Export successful",
            "data": {
                "path": "https://s3.eu-west-1.amazonaws.com/files.paystack.co/exports/463433/transactions/Integration_name_transactions_1724324423843.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAI7CL5IZL2DJHOPPA%2F20240822%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240822T110023Z&X-Amz-Expires=60&X-Amz-Signature=40525f4f361e07c09a445a1a6888d135758abd507ed988ee744c2d94ea14cf1e&X-Amz-SignedHeaders=host",
                "expiresAt": "2024-08-22 11:01:23"
            }
        }
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response

        response = self.transaction.export_transaction()

        mock_get.assert_called_with(
            f'https://api.paystack.co/transaction/export',
            headers=self.expected_headers,
            json=None,
            params=None
        )
        self.assertEqual(response, response_dict)

    @patch('requests.post')
    def test_partial_debit(self, mock_post):
        mock_response = Mock()
        response_dict = {
            "status": True,
            "message": "Charge attempted",
            "data": {
                "amount": 50000,
                "currency": "GHS",
                "transaction_date": "2024-08-22T11:13:48.000Z",
                "status": "success",
                "reference": "ofuhmnzw05vny9j",
            }
        }

        mock_response.json.return_value = response_dict

        mock_post.return_value = mock_response

        amount = 30
        email = 'mail@example.com'
        authorization_code = 'auth_code'
        currency = 'GHS'

        response = self.transaction.partial_debit(authorization_code, currency, amount, email)

        data = {
            'authorization_code':'auth_code',
            'currency':'GHS',
            'amount':'3000',
            'email':'mail@example.com'
        }

        mock_post.assert_called_with(
            f'https://api.paystack.co/transaction/partial_debit',
            headers=self.expected_headers,
            json=data,
            params=None
        )

if __name__ == '__main__':
    unittest.main()




