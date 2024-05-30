#!/usr/bin/python3

"""
class User that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    A city in the application.

    Attributes:
        name
        state_id
    """
    state_id = ""
    name = ""
