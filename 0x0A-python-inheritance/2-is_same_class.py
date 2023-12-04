#!usr/bin/python3

""" Exact same object """


def is_same_class(obj, a_class):
    """ Check if an object is an instance of a class.
    Args:
        obj (object): An object to check for.
        a_class (class): The class to reference with.
    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False.
    """

    return (type(obj) == a_class)
