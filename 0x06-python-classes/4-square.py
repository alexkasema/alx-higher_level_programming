#!/usr/bin/python3

""" Access and update private attribute """


class Square:
    """ A class that sets the properties getter and setter and
        calculates the area of the square
    """

    def __init__(self, size=0):
        """ Initialize an instance of a square.
        Args:
            size (int): The size of a square
        """
        self.size = size

    @property
    def size(self):
        """ Return size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the size of a square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculates the area of a square
        Return:
            The area of the square
        """
        return (self.__size ** 2)
