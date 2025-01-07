import json
from models.base_model import BaseModel

#!/usr/bin/python3
#Defines the FileStorage class for handling


class FileStorage:
 #Defines the FileStorage class for handling

    __file_path = "file.json"
    __objects = {}

    def all(self):
       #Defines the FileStorage class for handling

        return self.__objects

    def new(self, obj):
       #Defines the FileStorage class for handling

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        #Defines the FileStorage class for handling

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        #Defines the FileStorage class for handling

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = value["__class__"]
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error reloading objects: {e}")
            pass
