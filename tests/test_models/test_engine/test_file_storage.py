#!/usr/bin/python3
"""
Unittest for base module
"""
import json
import unittest
import os
import models
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
from models.city import City

class Test_FileStorage(unittest.TestCase):
    """ Test for
    File_Storage Class """

    def setUp(self):
        """ set up the
        test for testing File_Storage """
        pass

    def test_noarg(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_init(self):
        self.assertEqual(FileStorage, type(models.storage))

    def test_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_obj(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

class Test_FileStorage_m(unittest.TestCase):

    @classmethod
    def SetUp(self):
        try:
            os.rename("file.json", "copy_file.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("copy_file.json", "file_json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        models.storage.new(BaseModel())
        self.assertIn("BaseModel." + BaseModel().id, models.storage.all().keys())

    def test_new_all_cls(self):
        models.storage.new(Amenity())
        models.storage.new(Place())
        models.storage.new(User())
        models.storage.new(State())
        models.storage.new(Review())
        models.storage.new(City())
        self.assertIn("Amenity." + Amenity().id, models.storage.all().keys())
        self.assertIn("Place." + Place().id, models.storage.all().keys())
        self.assertIn("User." + User().id, models.storage.all().keys())
        self.assertIn("State." + State().id, models.storage.all().keys())
        self.assertIn("Review." + Review().id, models.storage.all().keys())
        self.assertIn("City." + City().id, models.storage.all().keys())


if __name__ == "__main__":
    unittest.main()
