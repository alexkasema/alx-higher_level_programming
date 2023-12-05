#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """ returns the dictionary description for JSON serialization of an object
    Args:
        obj (object): object to serialize.
    """
    return (obj.__dict__)
