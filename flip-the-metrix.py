def flipingmatrix(my_mat):
    sum = 0
    for i in range(4):
        for j in range(4):
            sum = max(max(my_mat[   i][j],))

matrix = []

for row in range(4):
    column_mat = []
    for column in range(4):
        val = int(input())
        column_mat.append(val)
    matrix.append(column_mat)



flipingmatrix(matrix)
