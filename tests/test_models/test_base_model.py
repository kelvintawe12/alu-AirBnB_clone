
#!/usr/bin/python3
from models.base_model import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

# Print initial instance details
print(my_model.id)
print(my_model)
print(type(my_model.created_at))

print("--")

# Convert instance to dictionary
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.items() or my_model_json.keys():
    print (f"\t{key}: ({type(my_model_json[key])}) - {my_model_json[key]}")

print("--")

# Create a new instance from the dictionary
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
# Check if the new instance is the same as the original
print(my_model is my_new_model)
