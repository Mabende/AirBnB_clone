#!/usr/bin/python3
"""
Review module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class represents a user's review of a place."""
    place_id = ""
    user_id = ""
    text = ""
