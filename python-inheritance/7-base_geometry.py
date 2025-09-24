#!/usr/bin/python3
"""
This module defines the BaseGeometry class with integer validation.
"""


class BaseGeometry:
    """
    A class representing base geometry.

    Methods:
        area(): Raises Exception (not implemented)
        integer_validator(name, value): Validates an integer value
    """

    def area(self):
        """
        Raises an Exception indicating that area is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
