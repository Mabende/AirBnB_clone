#!/usr/bin/python3
"""
test city
"""

from models.base_model import BaseModel
from models.city import City
import unittest
import models


class TestCity(unittest.TestCase):
    """
    test city case
    """
    def test_create_city(self):
        """
        test create city
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_city_state_id_default(self):
        """
        test city state id default
        """
        city = City()
        self.assertEqual(city.state_id, "")

    def test_city_name_default(self):
        """
        test city name default
        """
        city = City()
        self.assertEqual(city.name, "")

    def test_set_city_state_id(self):
        """
        test set city state id
        """
        city = City()
        city.state_id = "state_123"
        self.assertEqual(city.state_id, "state_123")

    def test_set_city_name(self):
        """
        test set city name
        """
        city = City()
        city.name = "New York City"
        self.assertEqual(city.name, "New York City")


if __name__ == '__main__':
    unittest.main()
