#!/usr/bin/python3
"""
MyList class module.
"""


class MyList(list):
    """
    A class that inherits from 'list' and adds a method for sorted printing.
    """

    def print_sorted(self):
        """
        Prints the list in sorted ascending order.
        """

        sorted_list = sorted(self)
        print(sorted_list)
