'''Найти все натуральные числа из промежутка от 1 до 200, у которых 
количество делителей равно N (N вводить с клавиатуры).'''

n = int(input("Введите число n "))
for i in range(1,200):
    counter = 2
    for j in range(2,int(i / 2) +1):
        if i % j == 0:
            counter += 1
    if counter  == n:
        print('Число :',i,'Делители: ',counter)
