#!/usr/bin/python3

import os.path
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
from models.city import City


class FileStorage:


    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FSobj_dict = FileStorage.__objects
        object_name = obj.__class__.__name__
        FSobj_dict["{}.{}".format(object_name, obj.id)] = obj

    def save(self):
        FSobjdict = FileStorage.__objects
        obj_dict = {obj: FSobjdict[obj].to_dict() for obj in FSobjdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as f:
                obj_dict = json.load(f)
                [self.new(BaseModel(**obj)) for obj in obj_dict.values()]
            return
