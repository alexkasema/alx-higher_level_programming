#!/usr/bin/python3

""" Printing a square """


class Square:
    """ A class that sets the properties getter and setter and
        calculates the area of the square and prints the square to stdout
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

    def my_print(self):
        """ Prints the square out the the stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
