from app.storage.storage import Storage

class CheckoutManager:
    """
    Manages the checkout and check-in of books.

    Attributes:
        storage (Storage): The storage instance for checkouts.
        checkouts (list): The list of checkouts managed.
    """

    def __init__(self, storage: Storage):
        """
        Initializes a CheckoutManager instance.

        Args:
            storage (Storage): The storage instance for checkouts.
        """
        self.storage = storage
        self.checkouts = self.storage.load()

    def checkout_book(self, user_id, isbn):
        """
        Records a book as checked out by a user.

        Args:
            user_id (str): The user ID of the user checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        self.checkouts.append({"user_id": user_id, "isbn": isbn})
        self.storage.save(self.checkouts)
        print("Book checked out successfully.")

    def checkin_book(self, user_id, isbn):
        """
        Records a book as checked in by a user.

        Args:
            user_id (str): The user ID of the user checking in the book.
            isbn (str): The ISBN of the book being checked in.
        """
        checkout = next((co for co in self.checkouts if co['user_id'] == user_id and co['isbn'] == isbn), None)
        if checkout:
            self.checkouts.remove(checkout)
            self.storage.save(self.checkouts)
            print("Book checked in successfully.")
        else:
            print("No matching checkout record found.")

    def list_checkouts(self):
        """
        Lists all current checkouts.
        """
        for checkout in self.checkouts:
            print(checkout)
        return self.checkouts
