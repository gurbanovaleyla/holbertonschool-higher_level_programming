#!/usr/bin/python3
"""This module defines a base geometry class."""


class BaseGeometry:
    """A base class for geometry operations."""

    def area(self):
        """Raise an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
