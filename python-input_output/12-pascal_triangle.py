#!/usr/bin/python3
"""Module for pascal_triangle method."""


def pascal_triangle(n):
    """Method that solves Pascal's triangle."""

    if n <= 0:
        return []

    # Initialize the triangle with 1's
    rows = [[1 for _ in range(i + 1)] for i in range(n)]

    for row_index in range(2, n):  # start from 3rd row (index 2)
        for col_index in range(1, row_index):
            # Each element is sum of two elements above it
            rows[row_index][col_index] = (
                rows[row_index - 1][col_index - 1]
                + rows[row_index - 1][col_index]
            )

    return rows
