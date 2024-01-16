#!/usr/bin/python3
"""test file_storade.py"""
import unittest
import json
import os
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from your_file_storage_module import FileStorag


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Reset __objects before each test
        FileStorage.__objects = {}

    def test_all(self):
        file_storage = FileStorage()
        # Check if all() returns an empty dictionary initially
        self.assertEqual(file_storage.all(), {})

        # Create some objects and add them to __objects
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        file_storage.new(obj1)
        file_storage.new(obj2)
        file_storage.new(obj3)

        # Check if all() returns the correct dictionary
        expected_result = {
            'BaseModel.' + obj1.id: obj1,
            'User.' + obj2.id: obj2,
            'State.' + obj3.id: obj3
        }
        self.assertEqual(file_storage.all(), expected_result)

    def test_save_reload(self):
        file_path = 'test_file.json'
        file_storage = FileStorage()
        file_storage.__file_path = file_path

        # Create some objects and add them to __objects
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        file_storage.new(obj1)
        file_storage.new(obj2)
        file_storage.new(obj3)

        # Save to file
        file_storage.save()

        # Check if the file exists and contains the correct data
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.assertEqual(len(data), 3)

        # Reset __objects and reload from file
        FileStorage.__objects = {}
        file_storage.reload()

        # Check if __objects is correctly reloaded
        expected_result = {
            'BaseModel.' + obj1.id: obj1,
            'User.' + obj2.id: obj2,
            'State.' + obj3.id: obj3
        }
        self.assertEqual(file_storage.all(), expected_result)

        # Clean up: Delete the test file
        os.remove(file_path)

    def test_file_path_attribute(self):
        file_storage = FileStorage()
        # Check if the __file_path attribute has the correct default value
        self.assertEqual(file_storage.__file_path, "file.json")

    def test_objects_attribute(self):
        file_storage = FileStorage()
        # Check if the __objects attribute is an empty dictionary initially
        self.assertEqual(file_storage.__objects, {})

        # Create some objects and add them to __objects
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        file_storage.new(obj1)
        file_storage.new(obj2)
        file_storage.new(obj3)

        # Check if __objects contains the correct objects
        expected_result = {
            'BaseModel.' + obj1.id: obj1,
            'User.' + obj2.id: obj2,
            'State.' + obj3.id: obj3
        }
        self.assertEqual(file_storage.__objects, expected_result)


if __name__ == '__main__':
    unittest.main()
