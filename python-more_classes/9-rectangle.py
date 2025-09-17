#!/usr/bin/python3
"""Class that defines a Rectangle"""


class Rectangle:
    """Represents a Rectangle with private width and height attributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle, validating width and height."""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if width or height
        is 0"""

        if self.width == 0 or self.height == 0:
            return 0

        return (self.width + self.height) * 2

    def __str__(self):
        """Return the rectangle drawn with '#' characters, or an empty
        string if width or height is 0"""

        if self.__width == 0 or self.__height == 0:
            return ""

        lines = str(self.print_symbol) * self.__width

        return "\n".join([lines for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater or equal area.

        Args:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.

        Returns:
            Rectangle: rect_1 if its area is >= rect_2's area, otherwise
            rect_2.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance where width == height == size"""

        return cls(size, size)
