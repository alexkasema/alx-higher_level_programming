#!/usr/bin/python3

def safe_print_division(a, b):
    """
    A function that divides 2 integers and prints the result.
    The result of the division should print on the finally:
    Returns the value of the division, otherwise: None
    """
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
