#!/usr/bin/python3
"""
module docs
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class that inherits from basemodel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
