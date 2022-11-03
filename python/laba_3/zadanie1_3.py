'''Найти все симметричные натуральные числа из промежутка от А до В (А 
и В вводятся с клавиатуры).'''

A = int(input("Введите число А "))
B = int(input("Введите число B "))

for i in range(A,B):
    t = str(i)
    flag = True
    for j in range(len(t) // 2):
        if t[j] != t[len(t) - j - 1]:
            flag = False
            continue
    if flag:
        print(i)
