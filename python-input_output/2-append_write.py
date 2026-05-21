#!/usr/bin/python3
"""
Module that appends a string to a UTF-8 text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Append a string at the end of a file and
    return number of chars added."""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
