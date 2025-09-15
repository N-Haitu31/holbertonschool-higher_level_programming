#!/usr/bin/python3
"""Defines a Square class with a private size attribute"""


class Square:
    """Represents a square with a private size"""

    def __init__(self, size=0):
        """Initialize a new Square with a
        private size attribute"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
