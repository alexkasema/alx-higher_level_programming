#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tup_a_len = len(tuple_a)
    tup_b_len = len(tuple_b)
    add = ()

    for i in range(2):
        if i >= tup_a_len:
            num1 = 0
        else:
            num1 = tuple_a[i]

        if i >= tup_b_len:
            num2 = 0
        else:
            num2 = tuple_b[i]

        if i == 0:
            add = (num1 + num2)
        else:
            add = (add, num1 + num2)

    return (add)
