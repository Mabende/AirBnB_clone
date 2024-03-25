#!/usr/bin/python3
"""
Test cases for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_id_length(self):
        """
        Test if the ID length is 36 characters.
        """
        obj = BaseModel()
        self.assertEqual(len(obj.id), 36)

    def test_id_type(self):
        """
        Test if the ID is of type string.
        """
        obj = BaseModel()
        self.assertIs(type(obj.id), str)

    def test_created_at_type(self):
        """
        Test if created_at attribute is of type datetime.
        """
        obj = BaseModel()
        self.assertIs(type(obj.created_at), datetime)

    def test_updated_at_type(self):
        """
        Test if updated_at attribute is of type datetime.
        """
        obj = BaseModel()
        self.assertIs(type(obj.updated_at), datetime)

    def test_to_dict_type(self):
        """
        Test if to_dict() method returns a dictionary.
        """
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        self.assertIsInstance(to_dict_dict, dict)

    def test_dict_type(self):
        """
        Test if dictionary returned by to_dict() method,
        contains 'id' key of type string.
        """
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        self.assertIsInstance(to_dict_dict["id"], str)

    def test_uuid_version(self):
        """
        Test if the UUID version is 4.
        """
        obj = BaseModel()
        to_uuid = UUID(obj.id)
        self.assertEqual(to_uuid.version, 4)

    def test_for_valid_id(self):
        """
        Test if the ID is a valid UUID.
        """
        obj = BaseModel()
        value = UUID(obj.id)
        self.assertIsInstance(value, UUID)

    def test_valid_to_dict(self):
        """
        Test if to_dict() method
        returns a valid dictionary with correct datetime formatting.
        """
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        created_at = datetime.fromisoformat(to_dict_dict["created_at"])
        updated_at = datetime.fromisoformat(to_dict_dict["updated_at"])

        self.assertEqual(to_dict_dict["updated_at"], updated_at.isoformat())
        self.assertEqual(to_dict_dict["created_at"], created_at.isoformat())
        self.assertIsInstance(to_dict_dict["updated_at"], str)
        self.assertIsInstance(to_dict_dict["created_at"], str)
        self.assertIn("updated_at", to_dict_dict)
        self.assertIn("created_at", to_dict_dict)


if __name__ == "__main__":
    unittest.main()
