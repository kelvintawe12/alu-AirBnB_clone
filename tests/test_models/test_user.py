#!/usr/bin/python3
"""Unit test for the User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up a new User instance before each test"""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "johndoe@example.com"

    def test_attributes(self):
        """Test User attributes"""
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "johndoe@example.com")


if __name__ == "__main__":
    unittest.main()
