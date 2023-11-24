#!/usr/bin/python3

""" Divide a matrix """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix.
    Args:
        matrix (list): A list containing int/floats to be divided.
        div (int, float): Number that divides each element of the list.
    Returns:
        A new matrix with the new numbers.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for num in [i for row in matrix for i in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [list(map(lambda num: round(num / div, 2), row)) for row in matrix]
