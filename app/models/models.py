class Book:
    """
    Represents a book with a title, author, and ISBN.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
    """

    def __init__(self, title, author, isbn):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def to_dict(self):
        """
        Converts the Book instance to a dictionary.

        Returns:
            dict: A dictionary representation of the book.
        """
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

    @staticmethod
    def from_dict(data):
        """
        Creates a Book instance from a dictionary.

        Args:
            data (dict): A dictionary with keys 'title', 'author', and 'isbn'.

        Returns:
            Book: A Book instance created from the dictionary.
        """
        return Book(data['title'], data['author'], data['isbn'])

    @staticmethod
    def validate_isbn(isbn):
        """
        Validates an ISBN.

        Args:
            isbn (str): The ISBN to validate.

        Returns:
            bool: True if the ISBN is valid, False otherwise.
        """
        return isbn.isdigit() and len(isbn) == 13


class User:
    """
    Represents a user with a name and user ID.

    Attributes:
        name (str): The name of the user.
        user_id (str): The user ID.
    """

    def __init__(self, name, user_id):
        """
        Initializes a User instance.

        Args:
            name (str): The name of the user.
            user_id (str): The user ID.
        """
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        """
        Converts the User instance to a dictionary.

        Returns:
            dict: A dictionary representation of the user.
        """
        return {"name": self.name, "user_id": self.user_id}

    @staticmethod
    def from_dict(data):
        """
        Creates a User instance from a dictionary.

        Args:
            data (dict): A dictionary with keys 'name' and 'user_id'.

        Returns:
            User: A User instance created from the dictionary.
        """
        return User(data['name'], data['user_id'])

    @staticmethod
    def validate_user_id(user_id):
        """
        Validates a user ID.

        Args:
            user_id (str): The user ID to validate.

        Returns:
            bool: True if the user ID is valid, False otherwise.
        """
        return user_id.isdigit()

