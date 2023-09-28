matrix = [[1, 2, 3], [4, 5, 6]]


def matrix_transposition(matrix):
    trans_matrix = [[matrix[i][j]
                     for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return trans_matrix


print(matrix_transposition(matrix))
