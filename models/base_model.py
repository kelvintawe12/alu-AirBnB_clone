''' the modelsclass'''
import uuid
from datetime import datetime
# from models import storage
from models.engine.file_storage import FileStorage


class BaseModel:
    ''' the modelsclass'''
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        self.args = args
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.storage = FileStorage()
            self.storage.new(self)  # Add a call to the method new(self) on storage

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Save'''
        self.updated_at = datetime.now()
        self.storage.save()  # Call save(self) method of storage

    def to_dict(self):
        '''To dict'''
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
