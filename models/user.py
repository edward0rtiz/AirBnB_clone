#!/usr/bin/python3
from base_model import BaseModel
"""Class that
represent
the user"""


class User(BaseModel):

    def __init__(self,):
        """Initialize user class
        instance
        of basemodel class"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
