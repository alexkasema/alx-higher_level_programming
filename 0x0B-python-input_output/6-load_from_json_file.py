#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”.
    Args:
        filename (file): Name of file to read from.
    """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
