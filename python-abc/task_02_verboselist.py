#!/usr/bin/env python3


class VerboseList(list):
    """
    Extends list and prints messages on append, extend, remove, and pop.
    """

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        n = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{n}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
