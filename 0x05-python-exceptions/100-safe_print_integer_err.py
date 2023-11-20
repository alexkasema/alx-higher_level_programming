#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    A function that prints an integer.
    value can be any type (integer, string, etc.).
    Returns True if value has been correctly printed.
    Otherwise, returns False and prints in stderr the error
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
