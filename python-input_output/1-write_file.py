#!/usr/bin/python3
"""This module writes a string to a text file (UTF8)
if it already exits and returns the number of characters written
otherwise creates the file if doesn't exist."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and
    returns the number of characters written."""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
