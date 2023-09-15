#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ rotate_2d_matrix(matrix) """
    
    l2 = []
    for i in range(len(matrix)):
        l2.append(print_column(matrix, i))
    print(l2)


def print_column(matrix, column_index):
    """ print column """
    l = []
    for row in matrix:
        if 0 <= column_index < len(row):
            l.append(row[column_index])
    return l[::-1]
