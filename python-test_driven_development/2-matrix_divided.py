#!/usr/bin/python3

"""
That divides all elements
"""


def matrix_divided(matrix, div):

    """
        Divide all element
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0 or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                        of integers/floats")

    new_matrix = []
    for row in matrix:
        new_row = []

        for element in row:
            result = round(element / div, 2)
            new_row.append(result)

        new_matrix.append(new_row)

    return new_matrix
