#!/usr/bin/python3
""" FileStorage """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent File storage engine"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        obj_f = FileStorage.__objects
        o_dict= {obj: obj_f[obj].to_dict() for obj in obj_f.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(o_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                o_dict = json.load(file)
                for obj_n in o_dict.values():
                    class_name = obj_n["__class__"]
                    del obj_n["__class__"]
                    self.new(eval(class_name)(**obj_n))
        except FileNotFoundError:
            return
