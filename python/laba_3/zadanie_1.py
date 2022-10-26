'''Дано натуральное число:
•   найти количество цифр данного числа;
•   верно ли, что данное число заканчивается на нечетную цифру.'''

import math
n = int(input('Введите число:'))
counter = 0
flag = True
if (n%2==0):
    flag = False

while n > 0:
    n = n // 10
    counter += 1

print('Цифр в числе:',counter)
print(flag)
