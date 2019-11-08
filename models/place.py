#!/usr/bin/python3
from base_model import BaseModel
"""Class that
represent
a Place"""


class Place(BaseModel):

    def __init__(self,):
        """Initialize place class
        instance
        of basemodel class"""
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
