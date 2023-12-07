#!/usr/bin/python3
""" unittest for Base class """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ sub class of TestCase """

    def test_instance_with_no_id_arg(self):
        """ test an instance with no id arg passed """
        a = Base()
        self.assertEqual(a.id, 1)

    def test_instance_with_id_arg(self):
        """ test an insance with id arg provided """
        a = Base(69)
        self.assertEqual(a.id, 69)

    def test_instance_with_wothout_id_arg(self):
        """ test instances where id is provided and not """
        a = Base(7)
        b = Base(2)
        c = Base()
        d = Base(4)
        e = Base()

        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, e.id - 1)
        self.assertEqual(a.id, 7)

    def test_public_instance_attr(self):
        """ test the public id instance attribute """
        a = Base()
        a.id = 10
        self.assertEqual(a.id, 10)

    def test_private_class_attr(self):
        """ test trying to access the private class attribute """

        with self.assertRaises(AttributeError):
            print(Base().__nb_instances)
