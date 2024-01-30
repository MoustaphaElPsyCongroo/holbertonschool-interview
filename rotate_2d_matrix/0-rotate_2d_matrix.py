#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix 90 degrees clockwise"""
    radius = len(matrix)
    rotated = [[] for x in range(radius)]

    for i in range(radius):
        for j in range(radius):
            rotated[i].append(matrix[radius - j - 1][i])

    for k in range(radius):
        for m in range(radius):
            matrix[k][m] = rotated[k][m]
