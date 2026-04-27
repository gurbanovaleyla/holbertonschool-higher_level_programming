#!/usr/bin/python3
"""
Dividing all elements of a matrix function module.

This module provides a function to divide all elements of a matrix.
Function handles edge cases like TypeError and ZeroDivisionError.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix and returns a new matrix.

    Args:
        matrix: a list of lists of integers or floats
        div: a number (integer or float)

    Returns:
        a new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of"
                    " lists) of integers/floats"
                )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
