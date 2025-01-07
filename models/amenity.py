from models.base_model import BaseModel

#!/usr/bin/python3
"""
Module for Amenity class
"""

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel
    """
    name = ""
    description = ""
    category = ""
    amenity_type = ""
    location = ""
    contact_info = ""
    image_url = ""
    user_id = ""
    created_at = ""
    updated_at = ""
    __init__ = __init__
    __repr__ = __repr__
    __str__ = __str__
    save_to_db = save_to_db
    delete_from_db = delete_from_db
    get_all_amenities = get_all_amenities
    get_amenity = get_amenity
    