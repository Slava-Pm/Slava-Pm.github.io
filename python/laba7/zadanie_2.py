'''type letters = set of 'a'..'z';
Описать процедуру print(А), печатающую в алфавитном порядке все элементы множества А, имеющего тип letters.Составить, программу, использующую эту процедуру.'''

def letters(str):
    alf = "abcdefghijklmnopqrstuvwxyz"
    alf = sorted(set(list(alf)))
    str = set(list(str))
    outset = set()
    for i in str:
        if i in alf:
            outset.add(i)
    return sorted(outset)

s = input('Введите строку: ')
print(letters(s))
