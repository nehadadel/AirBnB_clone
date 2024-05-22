#!/usr/bin/python3
""" FileStorage """
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent File storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        # Convert the objects to a serializable format
        serializable_objects = {}
        for key, value in FileStorage.__objects.items():
            serializable_objects[key] = value.to_dict()
        # Write to the JSON file
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(serializable_objects, json_file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as json_file:
                    serialized_objects = json.load(json_file)
                    FileStorage.__objects = {key: FileStorage._create_object(key, data) for key, data in serialized_objects.items()}

            except FileNotFoundError:
                pass
        else:
            pass

    @classmethod
    def _create_object(cls, key, data):
        """
        Helper method to create an object based on the key and data.
        """
        # Split the key to get class name and id
        class_name, obj_id = key.split('.')
        
        # Match the class name to the correct class and instantiate the object
        myclasses = {'BaseModel': BaseModel}
        if class_name in myclasses:
            return (myclasses[class_name](**data))
        else:
            raise ValueError("Unknown class name: {}".format(class_name))
