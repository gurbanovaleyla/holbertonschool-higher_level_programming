#!/usr/bin/python3
"""

This module provides a function to print a square with the character #.
Function handles edge cases like TypeError and ValueError.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: the size length of the square

    Returns:
        None
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
