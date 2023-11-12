#!/usr/bin/python3
""" the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent the City class.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
