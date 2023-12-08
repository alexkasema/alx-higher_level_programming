#!/usr/bin/python3
""" The Base class """
import json


class Base:
    """ Manages id attribute in all your future classes and to avoid
        duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization of base instance.
        Args:
            id (int): The id of a user
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of a list
        Args:
            list_dictionaries (list): list to serialize to json
        """

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")

        return (json.dumps(list_dictionaries))
