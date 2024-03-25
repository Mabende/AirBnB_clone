#!/usr/bin/python3
"""
Test cases for the Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def test_create_review(self):
        """
        Test if a Review instance can be created.
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes_default(self):
        """
        Test if default values are set for Review attributes.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_set_review_attributes(self):
        """
        Test if Review attributes can be set correctly.
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
