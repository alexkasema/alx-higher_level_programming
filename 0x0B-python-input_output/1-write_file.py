#!/usr/bin/python3

""" Write to a file """


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns the number
    of characters written.
    Args:
        filename (file): Name of file to write to.
        text (string): The text to write to the file.
    Return:
        Number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
