#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """transpose a 2D matrix 90 degrees clockwise"""
    n = len(matrix)
    mat_cp = [row[:] for row in matrix]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = mat_cp[n-1-j][i]
