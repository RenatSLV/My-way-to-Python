import math
"""
Реализовать инженерный калькулятор, для всех арифметических действий, включая 
нахождение факториала, Фибоначчи, и всех тригонометрических функций, также возведения 
числа в степени. 
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonnaci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

def calculator():
    print("Привет я могу тебе помочь")
    print("Вот что я умею:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (**)")
    print("6. Факториал (!)")
    print("7. Числа Фибоначчи (fib)")
    print("8. Синус (sin)")
    print("9. Косинус (cos)")
    print("10. Тангенс (tan)")
    print("11. Арксинус (asin)")
    print("12. Арккосинус (acos)")
    print("13. Арктангенс (atan)")

    while True:
        operation = input("Введи что хочешь сделать или напиши 'stop' для выхода: ").strip().lower()

        if operation == "stop":
            print("Пока:)")
            break
        if operation in ['+','-','*','/','**']:
            try:
                num1 = float(input("напиши первое число: "))
                num2 = float(input("напиши второе число: "))
                result = {
                    '+':lambda x,y: x + y,
                    '-':lambda x,y: x - y,
                    '*':lambda x,y: x * y,
                    '/':lambda x,y: x / y,
                    '**':lambda x,y: x ** y
                }[operation](num1,num2)
                print(f"Результат:{result}")
            except ValueError:
                print("пиши только цифры пожалуйста")
            except ZeroDivisionError:
                print("Не могу поделить на ноль:(")
        elif operation == "!":
            try:
                num = int(input("Напиши число: "))
                if num < 0:
                    print("Факториал могу найти только для неотрицательных числел.")
                else:
                    print(f"Результат:{factorial(num)}")
            except ValueError:
                print("пиши только цифры пожалуйста")
        elif operation == "fib":
            try:
                num = int(input("Напиши число: "))
                if num < 0:
                    print("фибоначи могу найти только для неотрицательных числел.")
                else:
                    print(f"Результат:{fibonnaci(num)}")
            except ValueError:
                print("пиши только цифры пожалуйста")
        elif operation in ["sin","cos","tan","asin","acos","atan"]:
            try:
                num = float(input("напиши число (в радианах): "))
                result = {
                    "sin": math.sin,
                    "cos": math.cos,
                    "tan": math.tan,
                    "asin": math.asin,
                    "acos": math.acos,
                    "atan": math.atan
                }[operation](num)
                print(f"Результат:{result}")
            except ValueError:
                print("пиши только цифры пожалуйста")
        else:
            print("Ты не правельно написал операцию или я не могу это решить")
calculator()