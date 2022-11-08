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

'''Дана матрица размера M × N. Удалить ее последний
столбец, содержащий только отрицательные элементы.'''
    
    
n = int(input())
m = int(input())

matrix = [0]*n;
for i in range(n):
    matrix[i] = [0]*m
    
for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input())
    
jmax = 0
for j in range(m):
    k = 0
    for i in range(n):
        if matrix[i][j] < 0:
            k += 1
    if k == n:
        jmax = j
        
for i in range(n):
    del matrix[i][jmax]
    
for i in range(n):
    for j in range(m-1):
        print(matrix[i][j], end = " ")
    print()  
    
'''Дана матрица размера M × N. Вставить в нее строку из
некоторого числа K перед строкой, среднеарифметическое
значение элементов которой максимально.'''

n = int(input())
m = int(input())

matrix = [0]*n;
for i in range(n):
    matrix[i] = [0]*m
    
for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input())
    
k = int(input())

maxavg = 0
for j in range(n):
    maxavg += matrix[0][j]
maxavg /= m
imaxavg = 0

for i in range(n):
    avg = 0
    for j in range(m):
        avg += matrix[i][j]
    avg /= m
    if avg> maxavg:
        maxavg = avg
        imaxavg = i
        
matrix1 = [0]*(n+1);
for i in range(n+1):
    matrix1[i] = [0]*m
        
for i in range(imaxavg):
    for j in range(m):
        matrix1[i][j] = matrix[i][j]      
        
for j in range(m):
    matrix1[imaxavg][j] = k

for i in range(imaxavg, n):
    for j in range(m):
        matrix1[i+1][j] = matrix[i][j]
        
# Итоговая матрица
        
for i in range(n+1):
    for j in range(m):
        print(matrix1[i][j], end=" ")
    print()
