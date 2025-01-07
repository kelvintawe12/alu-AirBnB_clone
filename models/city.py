from models.base_model import BaseModel

#!/usr/bin/python3
""" City Module for AirBnB project """

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize City class """
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
        self.save()
        self.save_to_file()
        self.id = self.update_id()
        self.save_to_json_file()
        self.save()
        print(f"City object created: {self.name}")
        return self
    
    def to_dict(self):
        """ Returns a dictionary representation of City """
        return {
            'state_id': self.state_id,
            'name': self.name
        }
    
    def update_id(self):
        """ Updates the id """
        return f"City.{self.id}"
    
    def save_to_file(self):
        """ Saves City instance to file """
        from models import storage
        storage.save()
        return True
    
    def save_to_json_file(self):
        """ Saves City instance to JSON file """
        from models import storage
        storage.save()
        return True
    
    @classmethod
    def load_from_file(cls, file_path):
        """ Loads City instance from file """
        from models import storage
        storage.reload()
        return True
    
    @classmethod
    def load_from_json_file(cls, file_path):
        """ Loads City instance from JSON file """
        from models import storage
        storage.reload()
        return True
    