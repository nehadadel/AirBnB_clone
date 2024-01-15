#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.

    Public class attributes:
    - name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
