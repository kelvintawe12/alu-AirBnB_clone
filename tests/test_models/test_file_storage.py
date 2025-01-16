#!/usr/bin/python3
"""Unit test for the FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up a new FileStorage instance before each test"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.name = "Test Model"
        self.model.save()
        self.storage.new(self.model)

    def test_all(self):
        """Test that all() returns the correct objects"""
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.model.id}", all_objects)

    def test_save_and_reload(self):
        """Test saving to and reloading from file"""
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.model.id}", all_objects)


if __name__ == "__main__":
    unittest.main()
