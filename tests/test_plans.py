import unittest
from pystack.plans import Plan
from decouple import config


class TestPlan(unittest.TestCase):
    def setUp(self):
        self.test_key = config('TEST_KEY')
        self.plan = Plan(self.test_key)
        
    def test_create_plan(self):
        name = 'Monthly retainer'
        interval = 'monthly'
        amount = 5000
        currency = 'GHS'

        response = self.plan.create_plan(name=name, amount=amount, interval=interval,currency=currency)

        data = {
            'name':'Monthly retainer',
            'interval':'monthly',
            'amount':500000,
            'currency':currency
        }

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Plan created')
        self.assertEqual(response['data']['name'], data['name'])
        self.assertEqual(response['data']['interval'], data['interval'])
        self.assertEqual(response['data']['amount'], data['amount'])
        self.assertEqual(response['data']['currency'], data['currency'])

    def test_list_plans(self):
        response = self.plan.list_plans()

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Plans retrieved')
        self.assertIsInstance(response['data'], list)

    def test_fetch_plan(self):
        id_or_code = 'PLN_3zt2onftk2z807h'

        response = self.plan.fetch_plan(id_or_code)

        self.assertEqual(response['status'], True)
        self.assertEqual(response['message'], 'Plan retrieved')
        self.assertEqual(response['data']['plan_code'], id_or_code)
        self.assertIsInstance(response['data'], dict)

    def test_update_plan(self):
        id_or_code = 'PLN_3zt2onftk2z807h'

        name = 'Monthly payment'
        amount = 5000
        interval = 'annually'

        response = self.plan.update_plan(id_or_code=id_or_code, name=name, amount=amount, interval=interval)

        self.assertEqual(response['status'], True)
        