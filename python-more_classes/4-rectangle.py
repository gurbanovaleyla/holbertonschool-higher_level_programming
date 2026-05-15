#!/usr/bin/python3
"""Defines a Rectangle class with width, height, and string representation."""


class Rectangle:
    """Represents a rectangle with validated width and height."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of rectangle using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rows = []
        for _ in range(self.__height):
            rows.append("#" * self.__width)

        return "\n".join(rows)

    def __repr__(self):
        """Return a string representation to create a rectangle instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
