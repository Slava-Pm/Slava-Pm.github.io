'''В одномерный массив, состоящий из п целых чисел вставить
новый элемент после всех минимальных элементов.'''

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
value = int(input())
mint = min(arr)
k = 0
for i in range(n):
    if arr[i] == mint:
        k +=1
for i in range(n+k):
    if arr[i] == mint:
        arr.insert(i+1,value)
print(arr)
