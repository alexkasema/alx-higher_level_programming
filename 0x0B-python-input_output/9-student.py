#!/usr/bin/python3
""" Student to JSON """


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

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """
        return (self.__dict__)
