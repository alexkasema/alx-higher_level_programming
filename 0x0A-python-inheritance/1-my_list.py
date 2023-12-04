#!/usr/bin/python3

""" My list """


class MyList(list):
    """ A class that inherits from lis class """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """

        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
