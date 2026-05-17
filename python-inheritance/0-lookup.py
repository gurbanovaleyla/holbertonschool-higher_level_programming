#!/usr/bin/python3
"""This module returns available attributes and methods of an object."""


def lookup(obj):
    """Return a list of an object's available attributes and methods."""
    return dir(obj)
