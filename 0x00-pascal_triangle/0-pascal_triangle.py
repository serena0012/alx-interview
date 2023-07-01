#!/usr/bin/python3
"""
Pascal's Triangle Solution
"""


def pascal_triangle(n):
    """
    Function returns a list of integers representing
    Pascal's Triangle of n.
    If n <= 0 returns an empty list.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for m in range(1, n):
        row = [1]
        for p in range(1, m):
            row.append(triangle[m - 1][p - 1] + triangle[m - 1][p])
        row.append(1)
        triangle.append(row)

    return triangle
