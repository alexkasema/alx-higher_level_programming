#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for r in matrix:
        r_len = len(r)
        for i in range(r_len):
            if i != r_len - 1:
                print("{}".format(r[i]), end=" ")
            else:
                print("{}".format(r[i]), end="")
        print()
