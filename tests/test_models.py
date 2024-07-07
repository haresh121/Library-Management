import unittest
from app.models.models import Book, User

class TestBook(unittest.TestCase):
    def test_to_dict(self):
        book = Book("Title", "Author", "1234567890123")
        self.assertEqual(book.to_dict(), {"title": "Title", "author": "Author", "isbn": "1234567890123"})

    def test_from_dict(self):
        data = {"title": "Title", "author": "Author", "isbn": "1234567890123"}
        book = Book.from_dict(data)
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.isbn, "1234567890123")

    def test_validate_isbn_valid(self):
        self.assertTrue(Book.validate_isbn("1234567890123"))

    def test_validate_isbn_invalid(self):
        self.assertFalse(Book.validate_isbn("12345678901"))
        self.assertFalse(Book.validate_isbn("abc"))

class TestUser(unittest.TestCase):
    def test_to_dict(self):
        user = User("Name", "123")
        self.assertEqual(user.to_dict(), {"name": "Name", "user_id": "123"})

    def test_from_dict(self):
        data = {"name": "Name", "user_id": "123"}
        user = User.from_dict(data)
        self.assertEqual(user.name, "Name")
        self.assertEqual(user.user_id, "123")

    def test_validate_user_id_valid(self):
        self.assertTrue(User.validate_user_id("123"))

    def test_validate_user_id_invalid(self):
        self.assertFalse(User.validate_user_id("abc"))
        self.assertFalse(User.validate_user_id(""))

if __name__ == '__main__':
    unittest.main()
