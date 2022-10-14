print("Введите три числа")
a, b, c = map(int,input().split())
if a>b and a>c and c>b:
    print(a,c,b)
elif a>b and a>c and b>c:
    print(a,b,c)
elif b>a and b>c and a>c:
    print(b,a,c)
elif b>a and b>c and c>a:
    print(b,c,a)
elif c>a and c>b and b>a:
    print(c,b,a)
elif c>a and c>b and a>b:
    print(c,a,b)
elif (a==b or a==c or b==c) and a>c: 
    print(a,b,c)
elif (a==b or a==c or b==c) and b>c: 
    print(b,c,a) 
elif (a==b or a==c or b==c) and c>a: 
    print(c,a,b) 
else:
    print(a,"=",b,"=",c)
                
