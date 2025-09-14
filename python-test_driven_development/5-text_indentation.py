#!/usr/bin/python3

"""
Text indentation
"""


def text_indentation(text):
    """
    add 2 lines after . ? and : charaters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ".?:":
        text = text.replace(delimiter, f"{delimiter}\n\n")

    lines = [line.strip() for line in text.split("\n\n")]

    print("\n\n".join(lines), end="")
