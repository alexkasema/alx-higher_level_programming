#!/usr/bin/python3
""" To JSON string """
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string).
    Args:
        my_object (list/dict): The object to serialize.
    """
    return (json.dumps(my_obj))
