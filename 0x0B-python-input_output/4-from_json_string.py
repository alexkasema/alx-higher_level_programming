#!/usr/bin/python3
""" From JSON string to Object """

import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string.
    Args:
        my_str (JSON string): The string to decode back to an object.
    """
    return (json.loads(my_str))
