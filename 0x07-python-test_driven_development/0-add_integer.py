#!/usr/bin/python3

""" Calculates the sum of two numbers """


def add_integer(a, b=98):
    """ Returns sum of a and b.
    Args:
        a (int, float): number argument.
        b (int, float): number argument.
    Returns:
        a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
