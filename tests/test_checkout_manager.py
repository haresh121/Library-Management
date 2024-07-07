import unittest
import os
from app.operations.check import CheckoutManager
from app.storage.storage import Storage

class TestCheckoutManager(unittest.TestCase):
    def setUp(self):
        self.checkout_storage = Storage('test_checkouts.json', dict)
        self.checkout_manager = CheckoutManager(self.checkout_storage)

    def tearDown(self):
        os.remove('test_checkouts.json')

    def test_checkout_book(self):
        self.checkout_manager.checkout_book("123", "1234567890123")
        self.assertEqual(len(self.checkout_manager.checkouts), 1)

    def test_checkin_book(self):
        self.checkout_manager.checkout_book("123", "1234567890123")
        self.checkout_manager.checkin_book("123", "1234567890123")
        self.assertEqual(len(self.checkout_manager.checkouts), 0)

    def test_list_checkouts(self):
        self.checkout_manager.checkout_book("123", "1234567890123")
        checkouts = self.checkout_manager.list_checkouts()
        self.assertIn({"user_id": "123", "isbn": "1234567890123"}, checkouts)

if __name__ == '__main__':
    unittest.main()
