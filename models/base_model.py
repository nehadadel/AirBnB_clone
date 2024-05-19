#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """
    def __init__(self):
        """
        init att
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return ("[{}]({}){}".format(class_name, self.id, self.__dict__))

    def save(self):
        """
        updates updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary  __dict__ of the instance:
        """
        dictionary_class = self.__dict__
        dictionary_class['__class__'] = self.__class__.__name__
        dictionary_class['created_at'] = self.created_at.isoformat()
        dictionary_class['updated_at'] = self.updated_at.isoformat()
        return dictionary_class
