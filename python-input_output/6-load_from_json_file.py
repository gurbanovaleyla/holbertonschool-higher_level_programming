#!/usr/bin/python3
"""
Module that creates a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
