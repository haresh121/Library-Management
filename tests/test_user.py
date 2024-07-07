import unittest
import os
from app.managers.user import UserManager
from app.storage.storage import Storage
from app.models.models import User

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_storage = Storage('test_users.json', User)
        self.user_manager = UserManager(self.user_storage)

    def tearDown(self):
        os.remove('test_users.json')

    def test_add_user_valid(self):
        self.user_manager.add_user("Name", "123")
        self.assertEqual(len(self.user_manager.users), 1)

    def test_add_user_invalid_user_id(self):
        self.user_manager.add_user("Name", "invalid_id")
        self.assertEqual(len(self.user_manager.users), 0)

    def test_find_user(self):
        self.user_manager.add_user("Name", "123")
        user = self.user_manager.find_user(user_id="123")
        self.assertIsNotNone(user)

    def test_update_user(self):
        self.user_manager.add_user("Name", "123")
        self.user_manager.update_user("123", name="New Name")
        user = self.user_manager.find_user(user_id="123")
        self.assertEqual(user.name, "New Name")

    def test_delete_user(self):
        self.user_manager.add_user("Name", "123")
        self.user_manager.delete_user("123")
        self.assertEqual(len(self.user_manager.users), 0)

if __name__ == '__main__':
    unittest.main()
