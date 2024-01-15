#!/usr/bin/python3
"""BaseModel Class"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel class for the airbnb """
    def __init__(self, *args, **kwargs):
        """ initialize BaseModel attributes"""
        if kwargs:
            for un_k, data_v in kwargs.items():
                if un_k == 'created_at' or un_k == 'updated_at':
                    data_v = datetime.strptime(data_v, "%Y-%m-%dT%H:%M:%S.%f")

                elif un_k == '__class__':
                    continue
                setattr(self, un_k, data_v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """reurn string representation of BaseModel """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ Update updated_at attribute with the current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return dictionary of BaseModel instance """
        dic_instance = self.__dict__.copy()
        dic_instance['created_at'] = self.created_at.isoformat()
        dic_instance['updated_at'] = self.updated_at.isoformat()
        dic_instance['__class__'] = self.__class__.__name__
        dic_instance = {key: value for key, value in dic_instance.items() if value}
        return dic_instance
