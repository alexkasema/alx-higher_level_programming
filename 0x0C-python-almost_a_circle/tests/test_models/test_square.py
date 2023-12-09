#!/usr/bin/python3
""" Tests for the square module """

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ subclass of TestCase to enable us do testing """

    def test_square(self):
        """ test square instance with correct values"""
        a = Square(2)
        self.assertEqual(a.area(), 4)

        a = Square(4, 2, 8, 1)
        self.assertEqual(str(a), "[Square] (1) 2/8 - 4")

    def test_square_getter_setter(self):
        """ test the getter and setter methods """
        a = Square(5)
        self.assertEqual(a.size, 5)

        a = Square(4)
        a.size = 10
        self.assertEqual(a.size, 10)
        self.assertEqual(a.area(), 100)

        with self.assertRaises(TypeError):
            a.size("two")

    def test_method_update_args(self):
        """ test the update methods with argument values"""
        a = Square(10, 10, 10, 10)
        a.update(6)
        self.assertEqual(a.id, 6)

        a.update(3, 9)
        self.assertEqual(a.size, 9)

        a.update(6, 9, 0)
        self.assertEqual(a.x, 0)

        a.update(4, 1, 4, 12)
        self.assertEqual(a.y, 12)

    def test_method_update_kwargs(self):
        """ test the update method with kwarg value """
        a = Square(10, 10, 10, 10)
        a.update(id=3)
        self.assertEqual(a.id, 3)

        a.update(x=7)
        self.assertEqual(a.x, 7)

        a.update(id=45, y=21)
        self.assertEqual(a.id, 45)
        self.assertEqual(a.y, 21)

    def test_method_to_dictionary(self):
        """ test the dict representation of a Square instance """
        a = Square(10, 2, 1, 1)
        a_dict = a.to_dictionary()
        self.assertEqual(a_dict, {'size': 10, "x": 2, "y": 1, "id": 1})

        with self.assertRaises(TypeError):
            a.to_dictionary(8)
