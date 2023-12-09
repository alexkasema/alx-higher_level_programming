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

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file
        Args:
            list_objs (objects): List of instances that inherit from Base
        """
        file_name = cls.__name__ + ".json"
        dict_list = []
        if list_objs is not None:
            dict_list = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary.
        Args:
            json_string (list): List of json strings.
        """

        if json_string is None or len(json_string) == 0:
            return ([])

        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        Args:
            dictionary (dict): a dict with key word as arguments.
        """
        if cls.__name__ == "Rectangle":
            my_class = cls(10, 10)
        else:
            my_class = cls(10)

        my_class.update(**dictionary)

        return (my_class)
