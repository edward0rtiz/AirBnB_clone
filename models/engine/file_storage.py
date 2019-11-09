#!/usr/bin/python3

import os.path
import json
from models.base_model import BaseModel

class FileStorage:


    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FSobjdict = FileStorage.__objects
        object_name = obj.__class__.__name__
        FSobjdict["{}. {}".format(object_name, obj.id)] = obj

    def save(self):
        FSobjdict = FileStorage.__objects
        obj_dict = {obj: FSobjdict[obj].to_dict() for obj in FSobjdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                [self.new(BaseModel(**obj)) for obj in obj_dict.values()]
            return
