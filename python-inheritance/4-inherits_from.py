#!/usr/bin/python3
"""This module checks if an object is an instance of a class
that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is a subclass instance of a_class,
    but not a direct instance."""
    return type(obj) is not a_class and isinstance(obj, a_class)
