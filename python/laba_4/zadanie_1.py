'''В одномерном массиве, состоящем из п целых элементов определить:
число соседств двух положительных чисел, двух чисел разного знака и двух чисел одного знака;
количество подряд идущих отрицательных элементов;
номер элемента, имеющего максимальное количество целочисленных делителей.
'''
n = (int(input()))
a=[]
for _ in range(n):
    a.append(int(input("Заполните массив ")))
count1 = 0
count2 = 0
count3 = 0
element = 1
maxmin = 0
delitel = 0
maxdel = 0
for i in range(n-1):
    if a[i]>0 and a[i+1]>0:
        count1 +=1
    if (a[i]>0 and a[i+1]<0) or (a[i]<0 and a[i+1]>0):
        count2 +=1
    if (a[i]>0 and a[i+1]>0) or (a[i]<0 and a[i+1]<0):
        count3 +=1
    
    if a[i]<0 and a[i+1]<0:
        element +=1
    elif maxmin<element:
        maxmin=element
        element=1
    else: 
        element=1
    for j in range(a[i]-1):
        if a[i]%(j+1) == 0:
            delitel +=1
    if maxdel<delitel:
        maxdel = delitel
        inter = i
        delitel = 0
    else:
        delitel = 0
        
print("число соседств двух положительных чисел = ",count1)
print("двух чисел разного знака = ",count2)
print("двух чисел одного знака = ",count3)
print("количество подряд идущих отрицательных элементов = ",maxmin)
print("номер эл-та с макс числом делителей = ",inter)
    
