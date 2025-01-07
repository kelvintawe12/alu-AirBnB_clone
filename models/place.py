from models.base_model import BaseModel

#!/usr/bin/python3
""" Place Module for AirBnB project """

class Place(BaseModel):
    """ A class Place that inherits from BaseModel """
    city_id = ""  # it will be the City.id
    user_id = ""  # it will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # it will be the list of Amenity.id
    review_ids = []  # it will be the list of Review.id
    def __init__(self, *args, **kwargs):
        """ Initializes Place object """
        super().__init__(*args, **kwargs)
        if 'city_id' in kwargs:
            self.city_id = kwargs['city_id']
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
            if not self.user_id:
                self.user_id = ""
        if 'name' in kwargs:
            self.name = kwargs['name']
            if not self.name:
                self.name = ""
                raise ValueError("name must be a non-empty string") 
            if not self.is_valid_name(self.name):
                raise ValueError("name must be a non-empty string")
            if len(self.name) > 100:
                raise ValueError("name must be a non-empty string")
            if not self.is_valid_string(self.name):
                raise ValueError("name must be a non-empty string")
        if 'description' in kwargs:
            self.description = kwargs['description']
            if not self.description:
                self.description = ""
            if not self.is_valid_string(self.description):
                raise ValueError("description must be a non-empty string")
        if 'number_rooms' in kwargs:
            self.number_rooms = kwargs['number_rooms']
            if not isinstance(self.number_rooms, int) or self.number_rooms < 0:
                raise ValueError("number_rooms must be a positive integer")
            if self.number_rooms > 100:
                raise ValueError("number_rooms must be a positive integer")
            if not self.is_valid_number(self.number_rooms):
                raise ValueError("number_rooms must be a positive integer")
        if 'number_bathrooms' in kwargs:
            self.number_bathrooms = kwargs['number_bathrooms']
            if not isinstance(self.number_bathrooms, int) or self.number_bathrooms < 0:
                raise ValueError("number_bathrooms must be a positive integer")
            if self.number_bathrooms > 100:
                raise ValueError("number_bathrooms must be a positive integer")
            if not self.is_valid_number(self.number_bathrooms):
                raise ValueError("number_bathrooms must be a positive integer")
        if 'max_guest' in kwargs:
            self.max_guest = kwargs['max_guest']
            if not isinstance(self.max_guest, int) or self.max_guest < 0:
                raise ValueError("max_guest must be a positive integer")
            if self.max_guest > 100:
                raise ValueError("max_guest must be a positive integer")
            if not self.is_valid_number(self.max_guest):
                raise ValueError("max_guest must be a positive integer")
    
    def is_valid_name(self, name):
        """ Validates the name attribute """
        return isinstance(name, str) and name.strip() != ""
    
    def is_valid_string(self, string):
        """ Validates the string attribute """
        return isinstance(string, str)
    # call the functions
    def is_valid_number(self, number):
        """ Validates the number attribute """
        return isinstance(number, int) and number >= 0  
    
