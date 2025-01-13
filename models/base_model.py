import uuid
from datetime import datetime
from models.engine.file_storage1 import FileStorage


class BaseModel:
    """BaseModel class that defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel."""
        if kwargs:
            # Load attributes from the dictionary `kwargs`
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    # Convert string to datetime object
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
        """Return a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update `updated_at` and save the instance to storage."""
        self.updated_at = datetime.now()
        self.storage.save()  # Save the updated instance in storage

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        result = self.__dict__.copy()  # Create a copy of the instance's attributes
        result["__class__"] = self.__class__.__name__  # Add the class name
        result["created_at"] = self.created_at.isoformat()  # Format `created_at` as ISO string
        result["updated_at"] = self.updated_at.isoformat()  # Format `updated_at` as ISO string
        return result
    