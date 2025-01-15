'''importation'''
import uuid
from models.base_model2 import BaseModel


class Review(BaseModel):
    '''doc'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'place_id' in kwargs:
            self.place_id = kwargs['place_id']
            if not isinstance(self.place_id, str):
                raise TypeError("place_id must be a string")
            if not self.place_id:
                raise ValueError("place_id cannot be empty")
        elif 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
            if not isinstance(self.user_id, str):
                raise TypeError("user_id must be a string")
            if not self.user_id:
                raise ValueError("user_id cannot be empty")
            if not self.get_or_create(BaseModel, id=self.user_id):
                raise ValueError("user_id must be a valid User.id")
        elif 'text' in kwargs:
            self.text = kwargs['text']
            if not isinstance(self.text, str):
                raise TypeError("text must be a string")
            if not self.text:
                raise ValueError("text cannot be empty")
        elif 'id' in kwargs:
            self.id = kwargs['id']
            if not isinstance(self.id, str):
                raise TypeError("id must be a string")
            if not self.id:
                raise ValueError("id cannot be empty")
        self.save()
        self.updated_at = self.get_updated_at()
        self.created_at = self.get_created_at()
        self.id = self.update_id()
        self.place_id = self.place_id

    def update_id(self):
        '''doc'''
        self.id = str(uuid.uuid4())
        return self.id

    def get_updated_at(self):
        '''doc'''
        return self.updated_at

    def get_created_at(self):
        '''doc'''
        return self.created_at
