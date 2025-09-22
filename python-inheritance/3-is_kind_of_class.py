#!/usr/bin/python3
"""
A module containing a function to check class type.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class or its subclasses.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the class or a subclass,
        otherwise False.
    """

    return isinstance(obj, a_class)
