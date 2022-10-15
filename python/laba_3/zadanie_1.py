import math
n = int(input('Введите число:'))
flag = True
if (n%2==0):
    flag = False
if n > 0:
    digits = int(math.log10(n))+1
elif n == 0:
    digits = 1
else:
    digits = int(math.log10(-n))+1
print('Цифр в числе:',digits)
print(flag)
