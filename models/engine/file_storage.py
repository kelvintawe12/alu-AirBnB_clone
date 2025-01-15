'''importation'''
import json


class FileStorage():
    """Class to store data in a file"""
    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store all objects

    def all(self):
        """Return the dictionary of stored objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            objects = json.load(f)
            for key, value in objects.items():
                cls_name = value["__class__"]
                # Re-creates objects using the appropriate class
                from models.base_model import BaseModel  # Import your model classes
                class_dict = {
                    "BaseModel": BaseModel,
                    # Add other classes here
                }
                self.__objects[key] = class_dict[cls_name](**value)
                self.__objects[key].id = key.split(".")[1]
            