#!/usr/bin/python3

""" Integer validator """


class BaseGeometry:
    """ A class with a method that validates a value. """

    def integer_validator(self, name, value):
        """ Validates the value given.
        Args:
            name (string): Name input.
            value (integer): Integer input.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")
