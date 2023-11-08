#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_keys = list(a_dictionary)
    my_keys.sort()
    for k in my_keys:
        print("{}: {}".format(k, a_dictionary[k]))
