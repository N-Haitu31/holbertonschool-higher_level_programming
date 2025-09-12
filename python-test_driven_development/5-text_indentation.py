#!/usr/bin/python3

"""
Text indentation
"""


def text_indentation(text):
    """
    add 2 lines after . ? and : charaters
    """
    if isinstance(text, str):
        new_text = ""
        for char in text:
            char = char.strip()
            if char in [".", "?", ":"]:
                new_text += "{}{}".format(char, "\n\n")
            else:
                new_text += char

        print(new_text)
    else:
        raise TypeError("text must be a string")
