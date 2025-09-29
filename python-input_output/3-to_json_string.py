#!/usr/bin/python3
"""
This module provides a function that returns
the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to convert.

    Returns:
        str: JSON string representation of the object.
    """

    return json.dumps(my_obj)
