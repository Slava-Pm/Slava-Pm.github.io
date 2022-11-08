'''Дана целочисленная матрица A(N, N), заполненная целыми
числами. Все ее положительные элементы записать в
одномерный массив, а остальные в другой.'''

n = int(input())

matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * n

arr1 = []
arr2 = []
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input())
        if matrix[i][j] > 0:
            arr1.append(matrix[i][j])
        else:
            arr2.append(matrix[i][j])

print('Ответ на первую задачу: ')
print(arr1)
print(arr2)

print("Наша матрица:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

'''Дана целочисленная матрица A(N, N), заполненная целыми
числами. Отсортировать по убыванию элементы матрицы,
расположенные над главной диагональю.'''

n = int(input())

matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * n
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input())
print("первоначальная матрица: ")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()


arr3 = []

for i in range(n):
    for j in range(n):
        if j > i:
            arr3.append(matrix[i][j])
arr3.sort(reverse=True)
k = 0
for i in range(n):
    for j in range(i, n):
        if j > i:
            matrix[i][j] = arr3[k]
            k += 1

print('Решение : ')
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end =' ')
    print()    
