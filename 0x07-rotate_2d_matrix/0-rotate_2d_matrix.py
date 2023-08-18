#!/usr/bin/python3
"""
Rotate 2D Matrix Module
"""


def rotate_2d_matrix(matrix):
    """
    Rotating n x n 2D matrix 90 degrees click-wise
    in place.
    """
    start = 0
    end = len(matrix) - 1
    while start < end:
        for i in range(start, end):
            layer = matrix[i][end]
            matrix[i][end] = matrix[start][i]
            layer2 = matrix[end][end + start - i]
            matrix[end][end + start - i] = layer
            layer = matrix[end + start - i][start]
            matrix[end + start - i][start] = layer2
            matrix[start][i] = layer
        start += 1
        end -= 1
