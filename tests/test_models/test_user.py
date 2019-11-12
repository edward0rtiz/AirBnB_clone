#!/usr/bin/python3
"""
Unittest for user module
"""
import os
import unittest
from models.user import User
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """ Test for
    User Class """

    def setUp(self):
        """set up the
        test for testing users"""
        pass

    def testpublic(self):
        self.assertEqual(str, type(User().id))


if __name__ == "__main__":
    unittest.main()
