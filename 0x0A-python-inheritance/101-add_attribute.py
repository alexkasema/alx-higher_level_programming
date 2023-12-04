#!/usr/bin/python3

""" Adding new attribute to an object if it’s possible """


def add_attribute(obj, name, value):
    """ A function that adds a new attribute to an object if it’s possible.
    Args:
        obj (object): The object to check if we can add attribute to.
        name (string): name of the attribute to add.
        value (): Value to add to the new attribute.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
