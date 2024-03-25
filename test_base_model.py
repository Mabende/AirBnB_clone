#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
json_type = type(my_model_json[key])
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, json_type, my_model_json[key]))
