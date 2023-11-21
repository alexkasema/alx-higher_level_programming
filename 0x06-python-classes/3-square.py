#!/usr/bin/python3

""" Area of a square """


class Square:
    """ A class that creates a square and claculates its area"""

    def __init__(self, size=0):
        """ Initializing a square instance.

        Args:
            size (int): The size of the square.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculates the current square area
        Returns:
            The area of the square
        """
        return (self.__size ** 2)
