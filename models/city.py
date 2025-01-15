'''import'''
from models.base_model2 import BaseModel


class City(BaseModel):
    '''class creation'''
    state_id = ""
    name = ""


def __init__(self, *args, **kwargs):
     ''' init method'''
     super().__init__(*args, **kwargs)
     self.state_id = kwargs.get('state_id', '')
     self.name = kwargs.get('name', '')
     self.save()
     self.save_to_file()
     self.id = self.update_id()
     self.save_to_json_file()
     self.save()
     print(f"City object created: {self.name}")


def to_dict(self):
        '''doc'''
        return {
            'state_id': self.state_id,
            'name': self.name
        }


def update_id(self):
        return f"City.{self.id}"


def save_to_file(self):
        from models.base_model2 import storage
        storage.save()
        return True


def save_to_json_file(self):
        '''ok'''
        from models import storage
        storage.save()
        return True


@classmethod
def load_from_file(cls, file_path):
        from models import storage
        storage.reload()
        return True


@classmethod
def load_from_json_file(cls, file_path):
        from models import storage
        storage.reload()
        return True
