#!/usr/bin/python3

def safe_print_integer(value):
    """
    A function that prints an integer with "{:d}".format().
    value can be any type (integer, string, etc.).
    Returns True if value has been correctly printed
    You have to use try: / except:
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
