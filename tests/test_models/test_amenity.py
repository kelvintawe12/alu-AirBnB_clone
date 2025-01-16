#!/usr/bin/python3
"""Unit test for the Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up a new Amenity instance before each test"""
        self.amenity = Amenity()
        self.amenity.name = "WiFi"

    def test_attributes(self):
        """Test Amenity attributes"""
        self.assertEqual(self.amenity.name, "WiFi")


if __name__ == "__main__":
    unittest.main()
