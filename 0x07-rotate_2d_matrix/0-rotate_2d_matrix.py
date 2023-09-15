#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ rotate_2d_matrix(matrix) """

    clone = matrix.copy()
    for i in range(len(clone)):
        matrix[i] = print_column(clone, i)


def print_column(matrix, column_index):
    """ print column """
    lis = []
    for row in matrix:
        if 0 <= column_index < len(row):
            lis.append(row[column_index])
    return lis[::-1]
