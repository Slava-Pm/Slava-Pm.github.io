'''Описать рекурсивную функцию NOD(A,B) целого типа, находящую наибольший общий делитель двух натуральных чисел A и B, 
используя алгоритм Евклида: NOD(A,B) = NOD(B mod A,A), если A <> 0; NOD(0,B) =
B. С помощью этой функции найти наибольшие общие делители пар A и B,
A и C, A и D, если даны числа A, B, C, D.'''

def gcd_recursion(num1, num2):
    if num1 == 0:
        return num2
    return gcd_recursion(num2 % num1, num1)


print(gcd_recursion(102, 256))
print(gcd_recursion(102, 306))
print(gcd_recursion(102, 482))
