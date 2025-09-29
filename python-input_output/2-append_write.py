#!/usr/bin/python3
"""
This module provides a function to write a string to a UTF8 text file.
"""


def write_file(filename="", text=""):
    """
    Appends a string at the end of a text
    file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to append.

    Returns:
        int: Number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
