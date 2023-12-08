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

    def update(self, *args, **kwargs):
        """ assigns values to attributes
        Args:
            args (int): list of no-keyword arguments
                1st argument should be the id attribute.
                2nd argument should be the size attribute.
                3rd argument should be the x attribute.
                4th argument should be the y attribute.
            kwargs (dict): a dictionary of keyword arguments.
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """ string representation of Square instance """
        string = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.x, self.y,
                                               self.width)
        return string
