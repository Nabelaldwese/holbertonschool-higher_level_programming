#!/usr/bin/python3
"""
Module for matrix_divided function.

This module divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Returns a new matrix with all elements divided by div,
    rounded to 2 decimal places.
    """
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix is list of lists
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    row_length = None

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
