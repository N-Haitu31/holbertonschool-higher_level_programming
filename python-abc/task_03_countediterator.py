#!/usr/bin/env python3


class CountedIterator:
    """
    Iterator that counts the number of items iterated.
    """

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        """
        Returns the number of items iterated over.
        """
        return self._count
