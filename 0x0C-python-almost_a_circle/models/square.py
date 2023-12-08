#!/usr/bin/python3
""" The square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a Square that inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing a square instance.
        Args:
            size (int): The size of the square.
            x (int): x-axis
            y (int): y-axis
            id (int): id value given to each square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ returns the size of the square """
        return (self.width)

    @size.setter
    def size(self, value):
        """ sets the size of the square """
        self.width = value
        self.height = value

    def __str__(self):
        """ string representation of Square instance """
        string = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.x, self.y,
                                               self.width)
        return string
