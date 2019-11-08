#!/usr/bin/python3
from uuid import uuid4
from json import dumps


class BaseModel:

    def __init__(self):
        """Initialize instances
        of basemodel class"""
        self.id = str(uuid4())
        self.created_at
