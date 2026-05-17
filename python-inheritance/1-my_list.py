#!/usr/bin/python3
"""This module contains a class that inherits out of a list
and prints the list in the ascending sort."""


class MyList(list):
    """A class inherits out of list."""
    def print_sorted(self):
        """Print list in the ascending order."""
        print(sorted(self))
