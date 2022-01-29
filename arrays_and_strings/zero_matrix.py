# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

# Time: O(n*m), Space: O(n)

def zero_matrix(matrix):
    row = [False] * len(matrix)
    column = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    for i in range(len(row)):
        if row[i]:
            nullifyRow(matrix, i)

    for j in range(len(column)):
        if column[j]:
            nullifyColumn(matrix, j)

    return matrix


def nullifyRow(matrix, row):
    for x in range(len(matrix[0])):
        matrix[row][x] = 0


def nullifyColumn(matrix, column):
    for y in range(len(matrix)):
        matrix[y][column] = 0
