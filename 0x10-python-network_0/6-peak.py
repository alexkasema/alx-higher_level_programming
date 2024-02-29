#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ Returns the peak in a list of integers. """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
