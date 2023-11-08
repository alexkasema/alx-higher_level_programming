#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is not None and type(a_dictionary) is dict:
        for key in list(a_dictionary):
            if a_dictionary[key] == value:
                del a_dictionary[key]
        return (a_dictionary)
