#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Initializes a FileStorage instance before each test."""
        self.storage = FileStorage()

    def tearDown(self):
        """Resets the class attributes to avoid side effects between tests."""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = 'file.json'

    def test_all(self):
        """Checks that all returns the correct initial dictionary."""
        self.assertEqual(self.storage.all(), {})
