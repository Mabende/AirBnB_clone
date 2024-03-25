#!/usr/bin/python3
"""
Module Docs
"""
import json
from models.base_model import BaseModel
from models.user import User
from os import path
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    parent class module that assigns storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        all instances
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new instances
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        save instances
        """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        load instances
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for key, value in json_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
