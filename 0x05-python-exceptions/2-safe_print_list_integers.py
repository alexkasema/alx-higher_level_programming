#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    A function that prints the first x elements of a list and only integers.
    All integers have to be printed on the same line followed by a new line.
    other type of value in the list must be skipped (in silence).
    """

    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return (count)
