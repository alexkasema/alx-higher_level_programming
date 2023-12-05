#!/usr/bin/python3

""" Append to a file """


def append_write(filename="", text=""):
    """ Appends to a file and returns number of characters added.
    Args:
        filename (file): The file to append  to.
        text (string): The text to add to the file.
    Return:
        Number of characters added to the file.
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
