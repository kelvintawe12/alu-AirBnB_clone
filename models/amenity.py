'''module importation'''
from models.base_model2 import BaseModel


class Amenity(BaseModel):
    '''Amenity class'''
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

    def __init__(self, *args, **kwargs):
        '''doc'''
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.category = kwargs.get('category')
        self.amenity_type = kwargs.get('amenity_type')
        self.location = kwargs.get('location')
        self.contact_info = kwargs.get('contact_info')
        self.image_url = kwargs.get('image_url')
        self.user_id = kwargs.get('user_id')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')
        self.save()
        self.save_to_file()
        self.id = self.update_id()
        self.save_to_json_file()
        return self

    def __str__(self):
        return f"{self.name}"

    def save_to_json_file(self):
        '''doc'''
        BaseModel.save_to_json_file([self])
        return True

    def update_id(self):
        '''doc'''
        return BaseModel.update_id()

    def save_to_file(self):
        '''doc'''
        return True

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'amenity_type': self.amenity_type,
            'location': self.location,
            'contact_info': self.contact_info,
            'image_url': self.image_url,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @classmethod
    def load_from_json_file(cls, filename):
        '''doc'''
        from models import storage
        storage.reload()
        return True
