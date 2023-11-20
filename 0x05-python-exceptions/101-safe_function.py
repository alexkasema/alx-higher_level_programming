#!/usr/bin/python3

def safe_function(fct, *args):
    """
    A function that executes a function safely.
    You can assume fct will be always a pointer to a function
    Returns the result of the function,
    Otherwise, returns None if something happens during the function and
    prints in stderr the error precede by Exception:
    """

    try:
        res = fct(*args)
        return (res)
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=stderr)
        return (None)
