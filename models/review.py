#!/usr/bin/python3
from base_model import BaseModel
"""Class that
represent
the review"""


class Review(BaseModel):

    def __init__(self,):
        """Initialize review class
        instance
        of basemodel class"""
        place_id = ''
        user_id = ''
        text = ''
