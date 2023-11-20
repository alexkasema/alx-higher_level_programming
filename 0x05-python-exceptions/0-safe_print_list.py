#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    A function that prints x elements of a list.
    Returns the real number of elements printed.
    """
    count = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            continue
    print()
    return (count)
