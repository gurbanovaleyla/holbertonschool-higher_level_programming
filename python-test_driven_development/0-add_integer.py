#!/usr/bin/python3
"""
Adding integers function module.

This module provides a function to add two integers.
Functions handle edge cases like TypeError for invalid inputs.
"""


def add_integer(a, b=98):
    """Adds two integers and returns the result.

    Args:
        a: first integer or float
        b: second integer or float, defaults to 98

    Returns:
        The integer addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
