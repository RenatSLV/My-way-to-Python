#наша функция
def myfunc(n):
    """
    функция котороя выдаёт на выход числа которые делятся на 7
    """
    for x in range(0, n+1):
        if x % 7 == 0:
            yield x

n = int(input("Введите число: "))
for number in myfunc(n):
    print(number)