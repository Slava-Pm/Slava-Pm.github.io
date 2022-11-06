''' Дана матрица размера M × N. Преобразовать матрицу,
поменяв местами минимальный и максимальный элемент в каждой
строке.'''

m, n = int(input()), int(input())

matrix = [0] * m
for i in range(m):
    matrix[i] = [0] * n

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input())

for i in range(n):
    elmax = 0
    elmin = 1000
    jn = 0
    jx = 0
    for j in range(m):
        if matrix[i][j] < elmin:
            elmin = matrix[i][j]
            jn = j
        if matrix[i][j] > elmax:
            elmax = matrix[i][j]
            jx = j
    matrix[i][jn], matrix[i][jx] = matrix[i][jx], matrix[i][jn]
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
