'''Даны три числа, не используя функции min и max, упорядочить их по убыванию.'''

print("Введите три числа")
a, b, c = map(float,input().split())
if (a>b and a>c and c>b) or (a==c and a>b):
    print(a,c,b)
elif (a>b and a>c and b>c) or (a==b and a>c) or (b==c and b<a):
    print(a,b,c)
elif (b>a and b>c and a>c) or (a==c and a<b):
    print(b,a,c)
elif (b>a and b>c and c>a) or (b==c and b>a):
    print(b,c,a)
elif c>a and c>b and b>a:
    print(c,b,a)
elif (c>a and c>b and a>b) or (a==b and a<c):
    print(c,a,b)
# Если все три числа имеют одинаковое значение
else:
    print(a,"=",b,"=",c)
