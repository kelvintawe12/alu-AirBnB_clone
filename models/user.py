'''module importation'''
from models.base_model import BaseModel


class User(BaseModel):
    '''creation of the classe'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.save()

    def save(self):
        self.create()
        return True

    def update(self, **kwargs):
        '''update function'''
        self.update()
        return True

    def delete(self):
        '''delete fonction'''
        self.delete()
        return True

    def create(self):
        '''create function'''
        self.save_to_db()
        return True

    def update(self):
        '''update'''
        self.save_to_db()
        return True