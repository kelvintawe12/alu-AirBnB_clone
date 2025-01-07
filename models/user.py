from models.base_model import BaseModel

#!/usr/bin/python3
#Defines the User class that inherits from BaseModel.
class User(BaseModel):
   
    #User class that represents a user in the AirBnB clone project.

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
       
        #Initializes the User class.
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.save()
    def save(self):
        # Saves the User object to the database.
        
        self.create()
        return True
    def update(self, **kwargs):
        #Updates the User object.
        self.update()
        return True
    def delete(self):
       
        #Deletes the User object from the database.
       
        self.delete()
        return True
    def create(self):
       
        #Creates the User object.
       
        self.save_to_db()
        return True
    def update(self):
       
        #Updates the User object.
       
        self.save_to_db()
        return True

user = User.objects.get(id=1)
print(user.id)
