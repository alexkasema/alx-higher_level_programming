#!/usr/bin/python3
""" Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing
        a specific string.
    Args:
        filename (file): The file to read and write to.
        search_string (string): The string to search for in the file.
        new_string (string): The string to add after every occurence.
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, mode="w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
