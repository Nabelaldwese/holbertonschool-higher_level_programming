#!/usr/bin/python3
"""Module that provides a function to return JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object."""
    return json.dumps(my_obj)
