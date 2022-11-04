'''В одномерном массиве, состоящем из п целых элементов удалить 
все отрицательные элементы.'''

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

i = 0
delarr = []  # массив индексов по которым в arr надо удалить элементы
for i in range(n):
    if arr[i] < 0:
        delarr.append(i)
for i in range(len(delarr)):
    del arr[delarr[i]]
print(*arr)
