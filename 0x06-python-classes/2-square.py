#!/usr/bin/python3

""" Size validation """


class Square:
    """ a class Square """

    def __init__(self, size=0):
        """ Initializing a square

        Args:
            size (int): size of square

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
