#!/usr/bin/python3

""" Printing a square """


class Square:
    """ A class that sets the properties getter and setter and
        calculates the area of the square and prints the square to stdout
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize an instance of a square.
        Args:
            size (int): The size of a square
            position (tuple): Position to print the squares
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Return size of the square """
        return (self.__size)

    @property
    def position(self):
        """ Return the position of where to print square """
        return (self.__position)

    @size.setter
    def size(self, value):
        """ Sets the size of a square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ set the coordinate position where to print the square """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
