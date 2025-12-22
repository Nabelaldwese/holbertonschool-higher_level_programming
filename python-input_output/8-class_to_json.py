#!/usr/bin/python3
"""Module for converting a class instance to a JSON-serializable dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization."""
    return obj.__dict__
