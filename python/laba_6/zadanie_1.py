'''Рассчитать значение z=max(a,2b)+max(2a-b,b) определив и использовав
функцию max(x,y) – максимальное из двух чисел.'''

def maxi(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Введите а: "))
b = int(input("Введите b: "))
z = 0
z = maxi(a, 2*b) + maxi(2 * a -b,b)
print(z)
