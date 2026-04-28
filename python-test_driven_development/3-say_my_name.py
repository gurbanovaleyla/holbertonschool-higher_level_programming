#!/usr/bin/python3
"""
This module provides a function to print the fullname of the person.
Function handles edge case like TypeError.
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>.

    Args:
        first_name(str): The first name of the person
        last_name(str): The last name of the person

    Returns:
        None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    result = "My name is {} {}".format(first_name, last_name)
    if last_name != ""
    else "My name is {}".format(first_name)
    print(result)
