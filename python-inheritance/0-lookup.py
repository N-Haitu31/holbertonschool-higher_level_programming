#!/usr/bin/python3
"""
This module defines the lookup function.

The lookup function returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """Return a list of an object's available attributes and methods"""

    attributes_and_methods = dir(obj)

    return attributes_and_methods
