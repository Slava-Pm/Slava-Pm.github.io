"""
Задача 1.(Общая для всех вариантов) Составить программу, задающую 4
множества, и демонстрирующую все операции над множествами.
"""
A = {4, 8, 7, 5}
B = {3, 4, 5, 2}
C = {7, 8, 5}
D = {8}

print("Объединение: ", A | C)
print("Разность: ", A - D)
print("Пересечение: ", C & B)
print("Симметрическая разность: ", A ^ B)

D.add(3) '''добавляет элемент в множество'''
print(D)
B.discard(4) '''удаляет из множества''' 
print(B)
A.clear() '''очищает множество'''
print(A)
