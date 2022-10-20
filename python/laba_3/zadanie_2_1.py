n = int(input("Введите число n "))

for i in range(1,200):
    counter = 0
    for j in range(1,int(i / 2) +1):
        if i % j == 0:
            counter += 1
    if counter + 1  == n:
        print('Число :',i,'Делители: ',counter+1)
