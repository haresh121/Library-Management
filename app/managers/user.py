from app.models.models import User
from app.storage.storage import Storage

class UserManager:
    """
    Manages a collection of users.

    Attributes:
        storage (Storage): The storage instance for users.
        users (list): The list of users managed.
    """

    def __init__(self, storage: Storage):
        """
        Initializes a UserManager instance.

        Args:
            storage (Storage): The storage instance for users.
        """
        self.storage = storage
        self.users = self.storage.load()

    def add_user(self, name, user_id):
        """
        Adds a user to the collection.

        Args:
            name (str): The name of the user.
            user_id (str): The user ID.
        """
        if not User.validate_user_id(user_id):
            print("Invalid User ID. Must be a numeric value.")
            return
        user = User(name, user_id)
        self.users.append(user)
        self.storage.save(self.users)
        print("User added successfully.")

    def list_users(self):
        """
        Lists all users in the collection.
        """
        for user in self.users:
            print(user.to_dict())

    def find_user(self, **kwargs):
        """
        Finds a user by given attributes.

        Args:
            **kwargs: Attributes to match (e.g., name, user_id).

        Returns:
            User: The found user, or None if no match is found.
        """
        for user in self.users:
            if all(getattr(user, k) == v for k, v in kwargs.items()):
                return user
        return None

    def update_user(self, user_id, **kwargs):
        """
        Updates attributes of a user.

        Args:
            user_id (str): The user ID of the user to update.
            **kwargs: The attributes to update.
        """
        user = self.find_user(user_id=user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self.storage.save(self.users)
            print("User updated successfully.")
        else:
            print("User not found.")

    def delete_user(self, user_id):
        """
        Deletes a user from the collection.

        Args:
            user_id (str): The user ID of the user to delete.
        """
        user = self.find_user(user_id=user_id)
        if user:
            self.users.remove(user)
            self.storage.save(self.users)
            print("User deleted successfully.")
        else:
            print("User not found.")
