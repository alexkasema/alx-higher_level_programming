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
        """ sets the value of width attribute
        Args:
            value (int): value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ returns height of the rectangle instance """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ sets the value of the height attribute
        Args:
            value (int): value of height
        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ return value of x attribute """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ sets the value of x attribute
        Args:
            value (int): Value of x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ return value of y attribute """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ sets the value of y attribute
        Args:
            value (int): value of y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area of a rectangle instance """
        return (self.__width * self.__height)

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ Assigns arguments to each attribute of rectangle instance
        Args:
            args (list):
                1st argument should be the id attribute.
                2nd argument should be the width attribute.
                3rd argument should be the height attribute.
                4th argument should be the x attribute.
                5th argument should be the y attribute.
            kwargs (dict): a dictionary that has attribute keys
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle instance"""
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        })

    def __str__(self):
        """ string representation of rectangle instance """
        string = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.x, self.y,
                                                  self.width, self.height)

        return string
