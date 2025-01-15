'''file path '''
#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# Reload all objects from the storage
storage = FileStorage()
storage.reload()

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id, obj in all_objs.items():
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
