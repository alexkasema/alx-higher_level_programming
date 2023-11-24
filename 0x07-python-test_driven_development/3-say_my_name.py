#!/usr/bin/python3

""" Say my name """


def say_my_name(first_name, last_name=""):
    """ A function that prints out names passed to it.
    Args:
        first_name (str): First name.
        last_name (str): Last name.
    Raises:
        TypeError exception if arguments are not strings

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
