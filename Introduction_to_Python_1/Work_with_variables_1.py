print("1")

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третье число: "))

sum = number_1 + number_2 + number_3
multi = number_1 * number_2 * number_3

print("Сумма",sum)
print("Произведение",multi)

print("2")

salary = int(input("Введите свою зарплату: "))
credit = int(input("Введите свои ежемесячный кредит: "))
communal_apartment = int(input("Введите свои коммунальные услуги: "))

the_rest_of_money = salary - (credit + communal_apartment)

print("Остаток",the_rest_of_money)

print("3")

diagonal_1 = int(input("Введите длину первой диагонали: "))
diagonal_2 = int(input("Введите длину второй диагонали: "))

S = 1 / 2 * diagonal_1 * diagonal_2

print("Площадь ромба", S)

print("4")

print("To be","or not","to be", sep="\n")

print("5")

print(
    ' "Life is what happens',
    "   when",
    "      you're busy making other plans",
    "\t\t\t\t\t\t\t\t  John Lennon.", sep="\n")
