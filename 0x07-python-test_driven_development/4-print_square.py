#!/usr/bin/python3

""" Print square """


def print_square(size):
    """ A function that prints a square with character #.
    Args:
        size (int): Length of the square.
    Raises:
        TypeError if size is not an Integer.
        ValueError if size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is bool:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
