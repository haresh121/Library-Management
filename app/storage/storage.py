import json
import os

class Storage:
    """
    Handles file-based storage and retrieval of objects.

    Attributes:
        filename (str): The name of the file for storage.
        obj_class (type): The class of objects to be stored and retrieved.
    """

    def __init__(self, filename, obj_class):
        """
        Initializes a Storage instance.

        Args:
            filename (str): The name of the file for storage.
            obj_class (type): The class of objects to be stored and retrieved.
        """
        self.filename = filename
        self.obj_class = obj_class
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """
        Ensures that the storage file exists, creating it if necessary.
        """
        if not os.path.exists(self.filename):
            with open(self.filename, 'w+') as file:
                json.dump([], file)

    def load(self):
        """
        Loads objects from the storage file.

        Returns:
            list: A list of objects loaded from the storage file.
        """
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return [self.obj_class.from_dict(item) for item in data]

    def save(self, items):
        """
        Saves objects to the storage file.

        Args:
            items (list): A list of objects to be saved.
        """
        with open(self.filename, 'w') as file:
            json.dump([item if isinstance(item, dict) else item.to_dict() for item in items], file)
