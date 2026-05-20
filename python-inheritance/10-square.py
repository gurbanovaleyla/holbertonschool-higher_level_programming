#!/usr/bin/python3
"""This module represents Square class that
inherits out of Rectangle and finds area."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits out of Rectangle."""
    def __init__(self, size):
        """Initialize size."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of Square."""
        return self.__size * self.__size
