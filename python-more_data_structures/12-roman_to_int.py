#!/usr/bin/python3


def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0

    for ch in roman_string:
        curr = values.get(ch, 0)
        if curr == 0:
            return 0

        if prev < curr:
            total += curr - 2 * prev

        else:
            total += curr

        prev = curr

    return total
