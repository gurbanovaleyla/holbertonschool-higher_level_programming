#!/usr/bin/python3
"""
Module that returns dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """Return the dictionary representation of a class instance."""
    return obj.__dict__
