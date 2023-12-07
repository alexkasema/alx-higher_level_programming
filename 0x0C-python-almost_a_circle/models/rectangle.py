#!/usr/bin/python3
""" First Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Defining a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing an instance of a rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns width of the rectangle instance """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ sets the value of width attribute """
        self.__width = value

    @property
    def height(self):
        """ returns height of the rectangle instance """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ sets the value of the height attribute """
        self.__height = value

    @property
    def x(self):
        """ return value of x attribute """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ sets the value of x attribute """
        self.__x = value

    @property
    def y(self):
        """ return value of y attribute """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ sets the value of y attribute """
        self.__y = value