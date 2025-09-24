#!/usr/bin/python3
"""
This module defines the BaseGeometry class with integer validation.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing base geometry.

    Methods:
        area(): Raises Exception (not implemented)
        integer_validator(name, value): Validates an integer value
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """

        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
