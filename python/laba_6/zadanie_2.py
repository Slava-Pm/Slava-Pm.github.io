def compare(number):
    if ((number // 1000)+((number // 100) % 10)) == ((number % 10) + ((number // 10) % 10)):
        return True
    return False


for i in range(1000,10000):
    if compare(i):
        print(i)
