'''В одномерном массиве, состоящем из п целых элементов удалить 
все отрицательные элементы.'''

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

i = 0
d = [] 
for i in range(n):
    if arr[i] < 0:
        d.append(i)
for i in range(len(d)):
    del arr[d[i]]
print(*arr)
