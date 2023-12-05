#!/usr/bin/python3
""" Save Object to a file """

import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation.
    Args:
        my_obj (object): The object to serialize and write to a file.
        filename (file): Name of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
