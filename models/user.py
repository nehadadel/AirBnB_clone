#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.

    Public class attributes:
    - email: string - empty string
    - password: string - empty string
    - first_name: string - empty string
    - last_name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""
