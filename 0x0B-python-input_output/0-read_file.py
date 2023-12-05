#!/usr/bin/python3

""" Read a file """


def read_file(filename=""):
    """  reads a text file (UTF8) and prints it to stdout
    Args:
        filename (file): Name of file
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
