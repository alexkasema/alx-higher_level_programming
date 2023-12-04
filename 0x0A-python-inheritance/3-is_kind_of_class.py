#!/usr/bin/python3

""" Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """ Checks is an object is an instance of a class or instance of a class
        that inherits from it.
    Args:
        obj (object): The object to check for.
        a_class (class): The class to reference with.
    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class; otherwise False.
    """

    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return (True)
    return (False)
