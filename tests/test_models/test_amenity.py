#!/usr/bin/python3
"""
Test cases for the Amenity class.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import models


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_class_name(self):
        """
        Test if the class is named correctly.
        """
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")

    def test_inheritance(self):
        """
        Test if the class inherits from BaseModel.
        """
        amenity = Amenity()
        self.assertTrue(issubclass(amenity.__class__, BaseModel))

    def test_module_docs(self):
        """
        Test if the module has documentation.
        """
        module_doc = Amenity.__doc__
        self.assertGreater(len(module_doc), 0)

    def test_class_docs(self):
        """
        Test if the class has documentation.
        """
        class_doc = Amenity.__doc__
        self.assertGreater(len(class_doc), 0)

    def test_name_type(self):
        """
        Test if the name attribute is of type string.
        """
        amenity = Amenity()
        self.assertIs(type(amenity.name), str)


if __name__ == "__main__":
    unittest.main()
