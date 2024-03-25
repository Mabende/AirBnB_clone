#!/usr/bin/python3
"""
review tests
"""

from models.base_model import BaseModel
from models.review import Review
import unittest
import models


class TestReview(unittest.TestCase):
    """
    Test_review case
    """
    def test_create_review(self):
        """
        test create review
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes_default(self):
        """
        test review attributes default
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_set_review_attributes(self):
        """
        test set review attributes
        """
        review = Review()
        review.place_id = "place_123"
        review.user_id = "user_456"
        review.text = "A great place to stay!"

        self.assertEqual(review.place_id, "place_123")
        self.assertEqual(review.user_id, "user_456")
        self.assertEqual(review.text, "A great place to stay!")


if __name__ == '__main__':
    unittest.main()
