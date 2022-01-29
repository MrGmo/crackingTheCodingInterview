# Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer, write a method to rotate the image by 90 degrees. Can you do this in place?

# Time: O(n^2), Space: O(1)
def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix[::-1]
