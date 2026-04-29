#!/usr/bin/python3
"""
This module provides a function to print a text with two new lines
after each of these characters: ., ? and :.
It raises a TypeError if the input is not a string.
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each of these characters:
    ., ? and :.

    Args:
        text (str): The input text to process.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")

            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1
