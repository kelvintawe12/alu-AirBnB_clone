import json
import os

class FileStorage:
    """Class to handle object serialization and storage."""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects

    def all(self):
        """Return the dictionary of stored objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        # Ensure the file exists before writing to it
        if not os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
                json.dump({}, f)  # Create an empty JSON file

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        # Create the file if it doesn't exist
        if not os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
                json.dump({}, f)  # Create an empty JSON file

        # Deserialize the JSON file if it contains data
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            objects = json.load(f)
            for key, value in objects.items():
                cls_name = value["__class__"]
                # Dynamically import the appropriate class
                module = __import__("models." + cls_name.lower(), fromlist=[cls_name])
                cls = getattr(module, cls_name)
                self.__objects[key] = cls(**value)
