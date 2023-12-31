#!/usr/bin/python3
""" unittest for Rectangle class """
import unittest
from io import StringIO
from unittest.mock import patch
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

    def test_width_height_x_y_str(self):
        """ Test passing width or height as strings """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a = Rectangle("cat", 7)

        a = Rectangle(3, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a.height = "dog"

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a = Rectangle(3, 7, "my", 8)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            a = Rectangle(8, 9, 7, "car")

    def test_width_height_x_y_float(self):
        """ test when the arguments are a float """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a = Rectangle(3.7, 9)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a = Rectangle(3, 55, 5.7, 2)

        a = Rectangle(8, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            a.y = 8.1

        a = Rectangle(3, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a.height = 9.7

    def test_width_height_bool(self):
        """ test if arguments are a bool """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a = Rectangle(True, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a = Rectangle(3, 4, True, 8)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            a = Rectangle(4, 5, 7, False)

        a = Rectangle(5, 8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a.height = False

    def test_width_height_x_y_list(self):
        """ test if args are a list """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a = Rectangle([], 7)

        a = Rectangle(8, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a.x = [3, 8]

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a = Rectangle(5, [9])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            a = Rectangle(4, 8, 9, [8, 7, 5])

    def test_width_height_x_y_dict(self):
        """ test if arguments are a dictionary """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a = Rectangle({'id': 3}, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a = Rectangle(5, {'name': 'Luke'})

        a = Rectangle(4, 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a.x = {'year': 2000}

        a = Rectangle(5, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            a.y = {'name': 'Mike'}

    def test_width_height_x_y_tuple(self):
        """ test if args are tuples """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a = Rectangle((1, 7), 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a = Rectangle(4, (9, ))

        a = Rectangle(5, 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a.x = (3, 8, 9)

        a = Rectangle(9, 8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            a.y = (4, 7)

    def test_width_height_negative_values(self):
        """ test if args are negative """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a = Rectangle(-4, 9)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a = Rectangle(0, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            a = Rectangle(7, 0)

        a = Rectangle(5, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            a.height = -6

    def test_x_y_negative_values(self):
        """ test if args are negative """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            a = Rectangle(3, 5, -4, 9)

        a = Rectangle(7, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            a.y = -4

    def test_rectangle_area(self):
        """ test the area method """
        a = Rectangle(4, 6)
        self.assertEqual(a.area(), 24)

        a = Rectangle(5, 3)
        a.width = 12
        a.height = 2
        self.assertEqual(a.area(), 24)

        a = Rectangle(7, 8)
        with self.assertRaises(TypeError):
            a.area(5, 9)

    def test_rectangle_display(self):
        """ Test displaying the rectangle with # character """
        with patch("sys.stdout", new_callable=StringIO) as my_output:
            a = Rectangle(3, 4)
            a.display()

            res = my_output.getvalue()
            self.assertEqual(res, "###\n###\n###\n###\n")

    def test_rectangle_display_with_args(self):
        """ test if we give the display function an argument """
        a = Rectangle(5, 7)
        with self.assertRaises(TypeError):
            a.display(8)

    def test_method_display_with_x(self):
        """ test the display method with x value """
        with patch("sys.stdout", new_callable=StringIO) as my_output:
            a = Rectangle(2, 3, 2)
            a.display()
            res = my_output.getvalue()
            self.assertEqual(res, "  ##\n  ##\n  ##\n")

    def test_method_display_with_y(self):
        """ test the display method with y value """
        with patch("sys.stdout", new_callable=StringIO) as my_output:
            a = Rectangle(2, 3, 0, 3)
            a.display()
            res = my_output.getvalue()
            self.assertEqual(res, "\n\n\n##\n##\n##\n")

    def test_method_display_with_x_y(self):
        """ test the display method with x and y values """
        with patch("sys.stdout", new_callable=StringIO) as my_output:
            a = Rectangle(2, 3, 2, 3)
            a.display()
            res = my_output.getvalue()
            self.assertEqual(res, "\n\n\n  ##\n  ##\n  ##\n")

    def test_method_update_with_one_arg(self):
        """ test the update method """
        a = Rectangle(10, 10, 10, 10)
        a.update(89)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 10/10")

    def test_method_update_with_two_args(self):
        """ test the update method with two args """
        a = Rectangle(10, 10, 10, 10)
        a.update(89, 2)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 2/10")

    def test_method_update_with_three_args(self):
        """ test the update method with tree args """
        a = Rectangle(10, 10, 10, 10)
        a.update(89, 2, 3)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 2/3")

    def test_method_update_with_four_args(self):
        """ test the update method with four args """
        a = Rectangle(10, 10, 10, 10)
        a.update(89, 2, 3, 4)
        self.assertEqual(str(a), "[Rectangle] (89) 4/10 - 2/3")

    def test_method_update_with_five_args(self):
        """ test the update method with five args """
        a = Rectangle(10, 10, 10, 10)
        a.update(89, 2, 3, 4, 5)
        self.assertEqual(str(a), "[Rectangle] (89) 4/5 - 2/3")

    def test_method_update_kwargs_one(self):
        """ test the update method with kwargs values """
        a = Rectangle(10, 10, 10, 10)
        a.update(id=1)
        self.assertEqual(str(a), "[Rectangle] (1) 10/10 - 10/10")

    def test_method_update_kwargs_two(self):
        """ test the update method with kwargs values """
        a = Rectangle(10, 10, 10, 10)
        a.update(height=4, id=1)
        self.assertEqual(str(a), "[Rectangle] (1) 10/10 - 10/4")

    def test_rectangle_method_str_(self):
        """ test the str method of the Rectangle class """

        a = Rectangle(3, 4, 1, 8, 9)
        self.assertEqual(str(a), "[Rectangle] (9) 1/8 - 3/4")

    def test_method_update_kwargs_three(self):
        """ test the update method """
        a = Rectangle(10, 10, 10, 10)
        a.update(x=4, width=8, id=7)
        self.assertEqual(str(a), "[Rectangle] (7) 4/10 - 8/10")

    def test_method_update_kwargs_five(self):
        """ test the update method """
        a = Rectangle(10, 10, 10, 10)
        a.update(id=1, y=2, height=7, width=6, x=9)
        self.assertEqual(str(a), "[Rectangle] (1) 9/2 - 6/7")

    def test_method_to_dictionary(self):
        """test the dict representation of a Rectangle instance"""
        a = Rectangle(3, 6, 5, 1, 8)
        res = {'id': 8, 'width': 3, 'height': 6, 'x': 5, 'y': 1}
        self.assertEqual(a.to_dictionary(), res)

    def test_method_to_dictionary_using_update_method(self):
        """ test if the obj are same after update with same values"""
        a = Rectangle(10, 2, 1, 9)
        a_dict = a.to_dictionary()

        b = Rectangle(1, 1)
        b.update(**a_dict)

        self.assertNotEqual(a, b)

    def test_method_str(self):
        """ test method with only width an height """
        a = Rectangle(5, 7, 3, 2, 11)
        self.assertEqual(str(a), "[Rectangle] (11) 3/2 - 5/7")

        a = Rectangle(5, 7, 3, 0, 3)
        self.assertEqual(str(a), "[Rectangle] (3) 3/0 - 5/7")
