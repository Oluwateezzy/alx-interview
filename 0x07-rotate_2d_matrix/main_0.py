def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_2d_matrix(matrix))

# The matrix will be rotated in-place to:
# [
#    [7, 4, 1],
#    [8, 5, 2],
#    [9, 6, 3]
# ]
