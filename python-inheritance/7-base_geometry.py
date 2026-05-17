#!/usr/bin/python3
"""
Module that defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class with validation utilities.
    """

    def area(self):
        """
        Raises an Exception because area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): variable name
            value (int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """

        # STRICT integer check (rejects bool too)
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
