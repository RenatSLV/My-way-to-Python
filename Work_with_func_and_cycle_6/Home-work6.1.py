"""
программу, которая считывает с консоли числа (по одному в строке) до тех 
пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму 
квадратов всех считанных чисел. 
"""
numbers =[]
total_sum = 0

print("Вводите числа по строкам")

while True:
    try:
        number = int(input())
        numbers.append(number)
        total_sum += number

        if total_sum == 0:
            break

    except ValueError:
        print("Вводите числа!!!")

    sum_of_squares = sum(x**2 for x in numbers)
    
print(sum_of_squares)