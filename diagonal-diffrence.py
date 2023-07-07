import numpy 

def diagonalDifference(matrix):
    primary_diagonal = numpy.diag(matrix)
    secondry_diagonal = numpy.diag(numpy.fliplr(matrix))
    return abs(sum(primary_diagonal) - sum(secondry_diagonal))
    
matrix_row = int(input())

matrix = []

for row in range(matrix_row):
    column_mat = []
    for column in range(matrix_row):
        val = int(input())
        column_mat.append(val)
    matrix.append(column_mat)

print(diagonalDifference(matrix))




"""import numpy as np

def diagonalDifference(matrix):
    primary_diagonal = matrix[0][0]+matrix[1][1]+matrix[2][2]
    secondry_diagonal = matrix[0][2]+matrix[1][1]+matrix[2][0]
    return abs(primary_diagonal - secondry_diagonal)
    
matrix_row = int(input())

matrix = []

for row in range(matrix_row):
    column_mat = []
    for column in range(matrix_row):
        val = int(input())
        column_mat.append(val)
    matrix.append(column_mat)




print(diagonalDifference(matrix))
"""
