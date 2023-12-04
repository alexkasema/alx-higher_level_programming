#!/usr/bin/python3

""" A class Square That inherits from class Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defining a Square class that inherits from Rectangle """

    def __init__(self, size):
        """ Initialization of square object.
        Args:
            size (int): Length of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
