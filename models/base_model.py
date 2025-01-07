import uuid
from datetime import datetime

#!/usr/bin/python3
"""
BaseModel Module
This module defines the BaseModel class that serves as the foundation
for all other models in the AirBnB clone project.
"""

class BaseModel:
    """Defines the BaseModel class for all other models."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        If kwargs is provided, it sets the instance attributes from it.
        Otherwise, generates new id and timestamps.
        """
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

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` timestamp to the current time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance into a dictionary format.
        """
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
    
base = BaseModel()

print(base)