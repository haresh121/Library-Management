import unittest
import os
from app.managers.book import BookManager
from app.storage.storage import Storage
from app.models.models import Book

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_storage = Storage('test_books.json', Book)
        self.book_manager = BookManager(self.book_storage)

    def tearDown(self):
        os.remove('test_books.json')

    def test_add_book_valid(self):
        self.book_manager.add_book("Title", "Author", "1234567890123")
        self.assertEqual(len(self.book_manager.books), 1)

    def test_add_book_invalid_isbn(self):
        self.book_manager.add_book("Title", "Author", "invalid_isbn")
        self.assertEqual(len(self.book_manager.books), 0)

    def test_find_book(self):
        self.book_manager.add_book("Title", "Author", "1234567890123")
        book = self.book_manager.find_book(isbn="1234567890123")
        self.assertIsNotNone(book)

    def test_update_book(self):
        self.book_manager.add_book("Title", "Author", "1234567890123")
        self.book_manager.update_book("1234567890123", title="New Title")
        book = self.book_manager.find_book(isbn="1234567890123")
        self.assertEqual(book.title, "New Title")

    def test_delete_book(self):
        self.book_manager.add_book("Title", "Author", "1234567890123")
        self.book_manager.delete_book("1234567890123")
        self.assertEqual(len(self.book_manager.books), 0)

if __name__ == '__main__':
    unittest.main()
