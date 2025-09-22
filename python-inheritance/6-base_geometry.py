#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an area method.
"""


class BaseGeometry:
    """
    A class representing base geometry.

    Methods:
        area: Raises an Exception.
    """

    def area(self):
        """
        Raises an Exception indicating that area is not implemented.
        """

        raise Exception("area() is not implemented")
