print ('Введите переменные с клавиатуры')
x1,x2,x3,y1,y2,y3 = map(int,input().split())

a = (((x2 - x1)**2 +(y2 - y1)**2)**0.5)
print("Сторона a =", a)

b = (((x3 - x2)**2 +(y3 - y2)**2)**0.5)
print("Сторона b =", b)

c = (((x1 - x3)**2 +(y1 - y3)**2)**0.5)
print("Сторона c = ", c)

p = a+b+c
print("Пеpиметр = ",p)
pl = int(p/2) #Полупериметр

S = ((pl*(pl-a)*(pl-b)*(pl-c))**0.5)
print("Площадь = ",S)