#!/usr/bin/python3
"""
Unit test for the BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""

    def setUp(self):
        """Set up a new BaseModel instance before each test"""
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89

    def test_attributes(self):
        """Test that the BaseModel attributes are correctly set"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertEqual(self.my_model.name, "My_First_Model")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertIsInstance(self.my_model.created_at, type(self.my_model.updated_at))

    def test_to_dict(self):
        """Test the to_dict method"""
        my_model_json = self.my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json["name"], "My_First_Model")
        self.assertEqual(my_model_json["my_number"], 89)
        self.assertIn("__class__", my_model_json)
        self.assertEqual(my_model_json["__class__"], "BaseModel")

    def test_recreate_from_dict(self):
        """Test recreating a BaseModel from its dictionary representation"""
        my_model_json = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertNotEqual(self.my_model, my_new_model)  # Ensure they are different instances
        self.assertEqual(self.my_model.id, my_new_model.id)
        self.assertEqual(self.my_model.name, my_new_model.name)
        self.assertEqual(self.my_model.my_number, my_new_model.my_number)
        self.assertEqual(self.my_model.created_at, my_new_model.created_at)

    def test_instance_comparison(self):
        """Test that two BaseModel instances are not the same"""
        my_model_json = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertFalse(self.my_model is my_new_model)


if __name__ == "__main__":
    unittest.main()
