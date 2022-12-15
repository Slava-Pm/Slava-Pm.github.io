"""Дан текстовый файл на некотором языке. Требуется подсчитать сколько раз каждое слово входит
в этот текст и вывести десять самых часто употребляемых слов в этом тексте и количество их употреблений.
Используйте словарь, в котором ключ -- слово, а значение -- количество таких слов.
 Точки, запятые, вопросы и восклицательные знаки перед обработкой замените пробелами
Все слова приводите к нижнему регистру при помощи метода строки lower()."""

text = {}
fin = open("input.txt", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")


while True:
    s = fin.readline()
    s = s.replace(".", "")
    s = s.replace("?", " ")
    s = s.replace("!", " ")
    s = s.replace(",", " ")
    s = s.replace("—", " ")
    s = s.replace("-", " ")
    s.lower()
    s = s.strip()
    s = s.split()
    if not s:
        break

    for word in s:
        if word not in text:
            text[word] = 1
        elif word in text:
            text[word] += 1
sorted_key = sorted(text, key=text.get, reverse=True)
for i in range(10):
    str_to_write = sorted_key[i]+': '+str(text[sorted_key[i]])+'; '
    fout.write(str_to_write)
