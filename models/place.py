'''import'''
import json


class FileStorage:
    '''doc'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        # Returns the dictionary __objects.
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        # Serializes __objects to the JSON file (path: __file_path).
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        # Deserializes the JSON file to __objects, if it exists.
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                from models.base_model2 import BaseModel
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = value["__class__"]
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass
