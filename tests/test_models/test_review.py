#!/usr/bin/python3
"""
Unittest for review module
"""
import os
import unittest
from models.review import Review
from models.base_model import BaseModel


class Test_Review(unittest.TestCase):
    """ Test for
    Review Class """

    def setUp(self):
        """set up the
        test for testing Reviews"""
        pass

    def testpublic(self):
        self.assertEqual(str, type(Review().id))


if __name__ == "__main__":
    unittest.main()
