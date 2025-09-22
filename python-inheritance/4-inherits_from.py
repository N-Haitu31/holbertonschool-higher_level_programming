#!/usr/bin/python3
"""
A function to check if an object is an instance of a subclass.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited from
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is a subclass of a_class, False otherwise.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
