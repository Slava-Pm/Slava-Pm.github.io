'''Найти количество трехзначных чисел, сумма цифр которых равна А, а 
само число заканчивается цифрой В (А и В вводятся с клавиатуры).'''

from random import randint
A = (int(input('Введите А: ')))
B = (int(input('Введите В: ')))
n = randint(100,999)
if ((n // 100)+(n//10%10)+(n%10) == A) and (n%10 == B): 
    print("Коректное число")
else:
    print("Проверьте правильность введённого числа")
    print(n)
    
    