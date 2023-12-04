#!/usr/bin/python3

""" Lookup Function """


def lookup(obj):
    """ Returns list of available attributes and methods of an object.
    Args:
        obj (object): The object in which to get its attributes and methods.
    """
    return (dir(obj))
