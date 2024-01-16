#!/usr/bin/python3
"""test for amenity.py"""
import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Unittest for Amenity class"""
    def setUp(self):
        self.amenity = Amenity()

    def test_init(self):
        self.assertEqual(self.amenity.name, "")

    def test_new_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_args_notused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_str_representation(self):
        str_representation = str(self.amenity)
        self.assertIn("[Amenity]", str_representation)
        self.assertIn("'name': ''", str_representation)


if __name__ == '__main__':
    unittest.main()
