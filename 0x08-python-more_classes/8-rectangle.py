#!/usr/bin/python3

""" Compare rectangles """


class Rectangle:
    """ A class that defines a rectangle by width and height
        and methods that calulates area and perimeter of rectangle.
    """
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialization of a new rectangle.
        Args:
            width (int): The width of a rectangle.
            height (int): The height of a rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ print message when an instance of a Rectangle is deleted """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ retrieves the width of a rectangle """
        return self.__width

    @property
    def height(self):
        """ retrieves the height of a rectangle """
        return self.__height

    @width.setter
    def width(self, value):
        """ Sets the width of a rectangle.
        Args:
            value (int): The value to set the width to.
        Raises:
            TypeError if value is not an integer.
            ValueError if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the height of a rectangle.
        Args:
            value (int): The value to set the height to.
        Raises:
            TypeError if value is not an Integer
            ValueError if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculates the area of a rectangle.
        Returns:
            area.
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Calculate the perimeter of a rectangle.
        Returns:
            Perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares the areas of two rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """ returns the string representation of an object """

        if self.__width == 0 or self.__height == 0:
            return ("")

        line = str(self.print_symbol) * self.__width
        return ('\n'.join([line] * self.__height))

    def __repr__(self):
        """ return a string representation of the rectangle """
        return (f"Rectangle({self.__width}, {self.__height})")
