''' the modelsclass'''
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel:
    ''' the modelsclass'''
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # Set default attributes for a new instance
            self.id = str(uuid.uuid4())  # Generate a unique identifier
            self.created_at = datetime.now()  # Set current datetime as created_at
            self.updated_at = self.created_at  # Set updated_at to created_at initially
            self.storage = FileStorage()
            self.storage.new(self)  # Add the new instance to storage

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Save'''
        self.updated_at = datetime.now()
        self.storage.save()  # Save the updated instance in storage

    def to_dict(self):
        '''To dict'''
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
