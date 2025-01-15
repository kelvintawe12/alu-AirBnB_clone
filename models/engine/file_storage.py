'''importation'''
import json


class FileStorage:
    """Class for handling storage of objects in JSON format."""

    def __init__(self):
        """Initialize the FileStorage instance."""
        self.__file_path = "file.json"  # Path to the JSON file
        self.__objects = {}  # Dictionary to store all objects

    def all(self):
        """Return the dictionary of stored objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = value["__class__"]
                    # Re-creates objects using the appropriate class
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            # Do nothing if the file doesn't exist
            pass
        except Exception as e:
            # Handle any unexpected errors during reload
            print(f"Error reloading objects: {e}")
            pass
