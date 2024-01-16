#!/usr/bin/python3
"""test for base_model.py"""
import os
import models
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test the __init__ method"""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_created_at(self):
        """ Test the created_at"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """ Test the updated_at"""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method"""
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_args_notused(self):
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_save(self):
        """Test the save method"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test__with_kwargs(self):
        date_today = datetime.today()
        dt_i = date_today.isoformat()
        model = BaseModel(id="123", created_at=dt_i, updated_at=dt_i)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, date_today)
        self.assertEqual(model.updated_at, date_today)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_contrast_to_dict_dunder_dict(self):
        model = BaseModel()
        self.assertNotEqual(model.to_dict(), model.__dict__)


if __name__ == '__main__':
    unittest.main()
