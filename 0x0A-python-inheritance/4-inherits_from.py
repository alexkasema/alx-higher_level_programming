#!/usr/bin/python3

""" Only sub class of """


def inherits_from(obj, a_class):
    """ Checks if an object is an instance of a class or a subclass.
    Args:
        obj (object): An object of a class.
        a_class (class): A class to reference with.
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.

    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
