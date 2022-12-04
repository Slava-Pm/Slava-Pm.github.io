"""
Задача 3. Даны два слова. Вычеркнуть из первого слова те буквы, 
которые встречаются во втором слове
"""

s, w = input(), input()

S = set(s)
W = set(w)

for char in s:
    if char not in W:
        print(char, end="")
