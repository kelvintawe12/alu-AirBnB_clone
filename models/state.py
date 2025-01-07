from models.base_model import BaseModel

#!/usr/bin/python3
"""
Module state
Defines the State class that inherits from BaseModel
"""


class State(BaseModel):
    """
    State class for AirBnB clone
    Inherits from BaseModel
    """
    name = ""
    city_id = ""
    country_id = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize State instance
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name')
        self.city_id = kwargs.get('city_id')
        self.country_id = kwargs.get('country_id')
        self.save()
        self.save_to_file()
        self.id = self.update_id()
        self.save_to_json_file()
    def save_to_json_file(self):
        """
        Save the current State instance to a JSON file
        """
        BaseModel.save_to_json_file([self])
        return True
    
    def update_id(self):
        """
        Updates the id
        """
        return f"State.{self.id}"
    
state = State()
print(state.id)