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

    def __eq__(self, other):
        """ comparison for equality
        Args:
            other (Square): Object of type square to compare to
        Returns:
            bool:
                True if equal else false
            NotImplemented:
                if cant compare with the other object
        """
        if type(other) is not Square:
            return NotImplemented
        else:
            return (self.area() == other.area())

    def __ne__(self, other):
        """ compares for not equal
        Args:
            other (Square): Object of type square
        Returns:
            True if are of the two objects is not equal else false
        """
        if type(other) is not Square:
            return NotImplemented
        else:
            return (self.area() != other.area())

    def __gt__(self, other):
        """ compare if one object is grater than the other object
        Returns:
            True if first object is greater than other object
        """
        if type(other) is not Square:
            return NotImplemented
        else:
            return (self.area() > other.area())

    def __ge__(self, other):
        """ Compare two square objects if greater than or equal to
        Returns:
            True if first object if greater than or equal to else false
        """
        if type(other) is not Square:
            return NotImplemented
        else:
            return (self.area() >= other.area())

    def __lt__(self, other):
        """ Compare two square objects if one is less than the other
        Returns:
            True if area of first object is less than other object else false
        """
        if type(other) is not Square:
            return NotImplemented
        else:
            return (self.area() < other.area())

    def __le__(self, other):
        """ Compare two squares for less than or equal to in the size of area
        Returns:
            True if first object is less than or equal to else false
        """
        if type(other) is not Square:
            return NotImplemented
        else:
            return (self.area() <= other.area())
