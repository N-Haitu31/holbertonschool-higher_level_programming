#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Instantiation with width and height validated as positive integers.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
