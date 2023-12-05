#!/usr/bin/python3
""" Student to disk and reload """


class Student:
    """ Defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initialization of a student object.
        Args:
            first_name (string): first name of student.
            last_name (string): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return (self.__dict__)
        return {atr: getattr(self, atr) for atr in attrs if hasattr(self, atr)}

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance.
        Args:
            json (dict): A dictionary that has key and value to replace

        """
        for k, v in json.items():
            setattr(self, k, v)
