#!/usr/bin/python3
""" unittest for Rectangle class """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ subclass of TestCase to implement unittests"""

    def test_instance_of_Rectangle(self):
        """ test instance of rectangle is Base"""
        a = Rectangle(1, 5)
        self.assertIsInstance(a, Base)

    def test_width_getter(self):
        """ getting the width of rectangle """
        a = Rectangle(4, 6)
        self.assertEqual(a.width, 4)
        

    def test_height_getter(self):
        """ test trying to get the height """
        a = Rectangle(24, 12)
        self.assertEqual(a.height, 12)

    def test_private_attr_height(self):
        """ test accessing the private attribut height """
        a = Rectangle(2, 7)
        with self.assertRaises(AttributeError):
            print(a.__height)

    def test_incorrect_no_of_arguments(self):
        """ testing nimber of arguments passed """
        with self.assertRaises(TypeError):
            a = Rectangle()

        with self.assertRaises(TypeError):
            a = Rectangle(33)

        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 3, 4, 5, 6)

    def test_height_setter(self):
        """ test setting the value of the height attribute """
        a = Rectangle(3, 6)
        a.height = 8
        self.assertEqual(a.height, 8)

    def test_width_setter(self):
        """ test setting the width attribute """
        a = Rectangle(8, 43)
        a.width = 12
        self.assertEqual(a.width, 12)
