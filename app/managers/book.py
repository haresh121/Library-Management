from app.models.models import Book
from app.storage.storage import Storage

class BookManager:
    """
    Manages a collection of books.

    Attributes:
        storage (Storage): The storage instance for books.
        books (list): The list of books managed.
    """

    def __init__(self, storage: Storage):
        """
        Initializes a BookManager instance.

        Args:
            storage (Storage): The storage instance for books.
        """
        self.storage = storage
        self.books = self.storage.load()

    def add_book(self, title, author, isbn):
        """
        Adds a book to the collection.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        if not Book.validate_isbn(isbn):
            print("Invalid ISBN. Must be a 13-digit number.")
            return
        book = Book(title, author, isbn)
        self.books.append(book)
        self.storage.save(self.books)
        print("Book added successfully.")

    def list_books(self):
        """
        Lists all books in the collection.
        """
        for book in self.books:
            print(book.to_dict())

    def find_book(self, **kwargs):
        """
        Finds a book by given attributes.

        Args:
            **kwargs: Attributes to match (e.g., title, author, isbn).

        Returns:
            Book: The found book, or None if no match is found.
        """
        for book in self.books:
            if all(getattr(book, k) == v for k, v in kwargs.items()):
                return book
        return None

    def update_book(self, isbn, **kwargs):
        """
        Updates a book's attributes.

        Args:
            isbn (str): The ISBN of the book to update.
            **kwargs: The attributes to update.
        """
        book = self.find_book(isbn=isbn)
        if book:
            for key, value in kwargs.items():
                setattr(book, key, value)
            self.storage.save(self.books)
            print("Book updated successfully.")
        else:
            print("Book not found.")

    def delete_book(self, isbn):
        """
        Deletes a book from the collection.

        Args:
            isbn (str): The ISBN of the book to delete.
        """
        book = self.find_book(isbn=isbn)
        if book:
            self.books.remove(book)
            self.storage.save(self.books)
            print("Book deleted successfully.")
        else:
            print("Book not found.")
