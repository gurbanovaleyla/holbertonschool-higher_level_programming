#!/usr/bin/python3
"""
Student class with serialization and deserialization support.
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

        If attrs is a list of strings, filter keys.
        Otherwise return all attributes.
        """
        obj_dict = self.__dict__

        if isinstance(attrs, list):
            filtered = {}
            for key in attrs:
                if key in obj_dict:
                    filtered[key] = obj_dict[key]
            return filtered

        return obj_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        using a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
