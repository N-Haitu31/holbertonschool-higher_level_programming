#!/usr/bin/python3
"""Defines a Square class with a private size attribute"""


class Square:
    """Represents a square with a private size"""

    def __init__(self, size=0):
        """Initialize a new Square using
        the property setter"""
        self.size = size

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

    def area(self):
        """Return the current square area"""

        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character
        or an empty line if size is 0"""

        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                for j in range(self.__size):

                    print("#", end="")

                print()
