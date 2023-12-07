#!/usr/bin/python3
""" The Base class """


class Base:
    """ Manages id attribute in all your future classes and to avoid
        duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization of base instance.
        Args:
            id (int): The id of a user
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
