import unittest
from decouple import config
from pystack import Transfer


class TestTransfer(unittest.TestCase):
    def setUp(self):
        self.test_key = config('TEST_KEY')
        self.transfer = Transfer(self.test_key)

    #URL Not Available for Starter (Test) Business Account
    def test_initialize_transfer(self):
        amount = 5000
        recipient = 'RCP_gx2wn530m0i3w3m'

        response = self.transfer.initiate_transfer(amount, recipient)

        data = {
            'source': 'balance',
            'amount': 5000,
            'recipient': 'RCP_gx2wn530m0i3w3m'
        }

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Transfer initialized')
        self.assertEqual(response['data']['source'], data['source'])
        self.assertEqual(response['data']['amount'], data['amount'])
        self.assertEqual(response['data']['recipient'], data['recipient'])

    