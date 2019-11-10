#!/usr/bin/python3

import os.path
import json

class FileStorage:


    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        FSobjdict = self.__objects
        object_name = obj.__class__.__name__
        FSobjdict["{}.{}".format(object_name, obj.id)] = obj

    def save(self):
        FSobjdict = self.__objects
        obj_dict = {obj: FSobjdict[obj].to_dict() for obj in FSobjdict.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.place import Place
        from models.user import User
        from models.state import State
        from models.review import Review
        from models.city import City

        cls_d = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                 'City': City, 'Place': Place,
                 'Review': Review, 'State': State}

        if os.path.exists(self.__file_path):
            with open(self.__file_path) as f:
                obj_dict = json.load(f)
                [self.new(cls_d[obj['__class__']](**obj))
                 for obj in obj_dict.values()
                 if obj['__class__'] in cls_d]
            return
