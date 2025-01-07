from models.base_model import BaseModel


class User(BaseModel):
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
        self.update()
        return True

    def delete(self):
        self.delete()
        return True

    def create(self):
        self.save_to_db()
        return True

    def update(self):
        self.save_to_db()
        return True
user = User.objects.get(id=1)
print(user.id)