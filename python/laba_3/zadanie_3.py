import math
N = (int(input('Количество слагаемых для каждого аргумента х ')))
x1,x2 = map(int,input('Введите интервал значений х ').split())
k=0
m=0
s=0
h=0
if N == m:
    h=(x2-x1)/m
for k in range(1,N):
    for x in range(x1,h,x2):
        s=s+(x**(2*k))/(math.factorial(2*k))
    print(s)
