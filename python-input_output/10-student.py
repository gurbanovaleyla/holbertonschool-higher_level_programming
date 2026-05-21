#!/usr/bin/python3
"""
Student class definition with attribute filtering.
"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of Student instance.

        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned.
        """
        obj_dict = self.__dict__

        if isinstance(attrs, list):
            filtered_dict = {}
            for key in attrs:
                if key in obj_dict:
                    filtered_dict[key] = obj_dict[key]
            return filtered_dict

        return obj_dict
