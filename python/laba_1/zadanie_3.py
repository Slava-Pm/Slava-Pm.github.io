print("Введите x и y")
x,y = map(int,input().split())
print("Результат:")
print((x<=(-(1-y**2))*0.5 and x>=(1-y**2)*0.5) and y <=1 and y>=-1 % 1)
