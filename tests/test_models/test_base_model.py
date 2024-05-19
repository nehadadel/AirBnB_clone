import unittest
from datetime import datetime
from uuid import uuid4
from your_module import BaseModel  # Import your BaseModel class from your module


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test __init__ method"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test __str__ method"""
        model = BaseModel()
        expected_output = f"[BaseModel] ({model.id}){model.__dict__}"
        self.assertEqual(str(model), expected_output)

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        # Ensure the original dictionary is not modified
        self.assertNotIn('__class__', model.__dict__)
        self.assertNotIn('created_at', model.__dict__)
        self.assertNotIn('updated_at', model.__dict__)

