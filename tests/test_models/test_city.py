#!/usr/bin/python3
"""
Unittest for city module
"""
import os
import unittest
from models.city import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    """ Test for
    city Class """

    def setUp(self):
        """set up the
        test for testing cities"""
        pass

    def testpublic(self):
        self.assertEqual(str, type(City().id))


if __name__ == "__main__":
    unittest.main()
