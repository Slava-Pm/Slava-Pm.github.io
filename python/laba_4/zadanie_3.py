'''В одномерном массиве, состоящем из п целых элементов.
Упорядочить отрицательные элементы массива по неубыванию.
Дан целочисленный массив A размера N. Переписать в новый
целочисленный массив B все четные числа из исходного массива
(в том же порядке) и вывести размер полученного массива B и
его содержимое.'''

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
i = 0
d = []
for i in range(n):
    if arr[i] < 0:
        arr.sort()
print(arr)

'''Дан целочисленный массив A размера N. Переписать в новый
целочисленный массив B все четные числа из исходного массива
(в том же порядке) и вывести размер полученного массива B и
его содержимое.'''

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
B = []
for i in range(n):
    if A[i] % 2 == 0:
        B.append(A[i])
print(len(B))
print(B)