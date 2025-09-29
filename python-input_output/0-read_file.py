#!/usr/bin/python3
"""
This module provides a function to read
and print the contents of a UTF8 text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    Args:
        filename (str): The name of the file to read.
    """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    print(read_data)
