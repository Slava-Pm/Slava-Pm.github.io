

'''Для заданной целочисленной матрицы A(N, M) определите
сумму и количество элементов матрицы, кратных некоторому
числу a.
В каждом столбце заданной матрицы A(N, M) вычислите сумму
нечетных элементов.
 Дана квадратная матрица A(N, N) целых чисел. Найти сумму S1
элементов в последнем столбце матрицы. Определить количество
элементов под побочной  диагональю матрицы, значения
которых больше S1.'''

n, m = int(input('n - ')), int(input('m - '))
mat = [0]*n
for i in range(n):
    mat[i] = [0]*m
for i in range(n):
    for j in range(m):
        mat[i][j] = int(input())
print("Наша матрица:")
for i in range(n):
    for j in range(m):
        print(mat[i][j], end=" ")
    print()
k = 0
sum = 0

a = int(input('Введите число a - '))
for i in range(n):
    for j in range(m):
        if mat[i][j] % a == 0 and mat[i][j] != 0:
            sum += mat[i][j]
            k += 1
print("Сумма элементов, кратных числу ",a,"= ",sum,"Кол-во таких элементов - ",k)
sumnechet = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] < 0:
            for i in range(n):
                sumnechet += mat[i][j]
        print("Cумма нечетных элементов",sumnechet)