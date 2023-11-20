#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    A function that divides element by element 2 lists.
    my_list_1 and my_list_2 can contain any type (integer, string, etc.).
    list_length can be bigger than the length of both lists.
    If 2 elements can’t be divided, the division result should be equal to 0.
    Returns a new list (length = list_length) with all divisions
    """

    new = []
    res = 0

    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new.append(res)
    return (new)
