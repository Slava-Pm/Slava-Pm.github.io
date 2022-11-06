'''Дана целочисленная матрица A(N, N), заполненная целыми
числами. Все ее положительные элементы записать в
одномерный массив, а остальные в другой.
Дана целочисленная матрица A(N, N), заполненная целыми
числами. Отсортировать по убыванию элементы матрицы,
расположенные под главной диагональю.'''

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
