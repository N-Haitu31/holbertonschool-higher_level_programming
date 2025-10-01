#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student instance.
        If attrs is a list of strings, only return those attributes.
        Otherwise, return all attributes.
        """

        if attrs is None:
            return self.__dict__.copy()

        filtered = {}
        for attr in attrs:
            if attr in self.__dict__:
                filtered[attr] = self.__dict__[attr]
        return filtered

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with json dict."""

        for key, value in json.items():
            setattr(self, key, value)
