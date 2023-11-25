#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """  unittests for max_integer fuction """

    def test_empty_list(self):
        """ tests an empty list """
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_one_element(self):
        """ test for the case of one element """
        test_list = [55]
        self.assertEqual(max_integer(test_list), 55)

    def test_positive_numbers(self):
        """ Test for the case of positive numbers in the list """
        test_list = [3, 1, 7, 4, 9, 18, 2]
        self.assertEqual(max_integer(test_list), 18)

    def test_negative_numbers(self):
        """ Test for the case list has negative numbers """
        test_list = [-5, -66, -7, -32, -8]
        self.assertEqual(max_integer(test_list), -5)

    def test_positive_negative(self):
        """ Test for case of both positive abd negative numbers """
        test_list = [4, -4, 9, -3, -5, 2]
        self.assertEqual(max_integer(test_list), 9)

    def test_float_numbers(self):
        """ Test for the case of float numbers """
        test_list = [-2.3, -5.87, -90, -4]
        self.assertEqual(max_integer(test_list), -2.3)

    def test_string(self):
        """ Test for the case a string is passed """
        test_list = "Hello"
        self.assertEqual(max_integer(test_list), "o")

    def test_list_strings(self):
        """ Test for case a list of strings is passed """
        test_list = ["Alex", "Mike", "Kate"]
        self.assertEqual(max_integer(test_list), "Mike")
