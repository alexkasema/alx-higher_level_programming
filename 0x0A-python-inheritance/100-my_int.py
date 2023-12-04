#!/usr/bin/python3

""" My integer """


class MyInt(int):
    """ A class that inherits from int class """

    def __eq__(self, other):
        """ Implement equality for MyInt class objects.
        Args:
            other (int): The value to compare to.
        """
        return (int(self) != other)

    def __ne__(self, other):
        """ Implement not equal for MyInt class objects.
        Args:
            other (int): The value to compare to.
        """

        return (int(self) == other)
