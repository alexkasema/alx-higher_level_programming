#!/usr/bin/python3

""" A class that inherits from another class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defining a rectangle class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initializing an instance of a Rectangle.
        Args:
            width (integer): width of rectangle.
            height (integer): height of rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
