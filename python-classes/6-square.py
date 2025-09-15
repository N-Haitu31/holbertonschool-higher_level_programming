#!/usr/bin/python3
"""Defines a Square class with a private size attribute"""


class Square:
    """Represents a square with private size
    and position, area calculation, and printing"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square, validating
        size and position via setters"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with
        validation"""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current square area"""

        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character
        or an empty line if size is 0"""

        if self.__size == 0:
            print()

        else:
            # vertical offset
            for _ in range(self.__position[1]):
                print()

            # rows with horizontal offset
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
