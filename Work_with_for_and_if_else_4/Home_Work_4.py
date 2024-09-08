"""
программу, которая помогает найти минимальное подходящее число. 
"""
#ввод чисел для работы
num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
total = num1 * num2

#цикл и срвзу же сюда условие 
while num1!=0 and num2!=0:
    if num1 > num2:
        num1 %= num2
    else:
        num2 %= num1
        
#Ввывод данных
print(total / ( num1 + num2 ))
