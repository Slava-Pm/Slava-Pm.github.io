A = int(input("Введите число А "))
B = int(input("Введите число B "))

for i in range(A,B):
    temp = str(i)
    flag = True
    for j in range(len(temp) // 2):
        if temp[j] != temp[len(temp) - j - 1]:
            flag = False
            continue
    if flag:
        print('this is paly!',i)
