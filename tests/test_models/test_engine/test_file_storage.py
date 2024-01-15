#!/usr/bin/python3
"""tests for file_storage.py"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Create instances of classes for testing"""
        self.user = User()
        self.state = State()
        self.city = City()
        self.place = Place()
        self.amenity = Amenity()
        self.review = Review()

        self.user.id = "user_id"
        self.state.id = "state_id"
        self.city.id = "city_id"
        self.place.id = "place_id"
        self.amenity.id = "amenity_id"
        self.review.id = "review_id"
        self.file_storage = FileStorage()

    def test_FileStorage_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_new_with_args(self):
         with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_empty(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        model = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(model)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as fil:
            save_text = fil.read()
            self.assertIn("BaseModel." + model.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + ct.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_reload(self):
        model= BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(model)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + model.id, obj)
        self.assertIn("User." + us.id, obj)
        self.assertIn("State." + st.id, obj)
        self.assertIn("Place." + pl.id, obj)
        self.assertIn("City." + ct.id, obj)
        self.assertIn("Amenity." + am.id, obj)
        self.assertIn("Review." + rv.id, obj)
if __name__ == '__main__':
    unittest.main()
