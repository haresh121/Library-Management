import unittest
import os
from app.storage.storage import Storage
from app.models.models import Book, User

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.book_storage = Storage('test_books.json', Book)
        self.user_storage = Storage('test_users.json', User)

    def tearDown(self):
        os.remove('test_books.json')
        os.remove('test_users.json')

    def test_load_empty(self):
        books = self.book_storage.load()
        self.assertEqual(books, [])

    def test_save_and_load(self):
        book = Book("Title", "Author", "1234567890123")
        self.book_storage.save([book])
        books = self.book_storage.load()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Title")

if __name__ == '__main__':
    unittest.main()
