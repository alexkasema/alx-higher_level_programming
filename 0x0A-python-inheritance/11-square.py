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

    def area(self):
        """ Calculates the area of a square """
        return (self.__size ** 2)

    def __str__(self):
        """ Returns string representation of a square object """
        return "[Square] {}/{}".format(self.__size, self.__size)
