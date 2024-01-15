#!/usr/bin/python3
"""State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.

    Public class attributes:
    - name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
