#!/usr/bin/python3
"""
city module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class represents a city within a state."""
    state_id = ""
    name = ""
