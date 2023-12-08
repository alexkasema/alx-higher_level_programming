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
