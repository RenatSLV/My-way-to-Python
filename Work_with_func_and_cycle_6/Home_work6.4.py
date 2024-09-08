"""
Пользователь вводит с клавиатуры название производителя 
и слово для замены.
"""

car_name = (
    "BMW",
    "Toyota",
    "Audi",
    "Mercedec-Benz",
    "Honda",
    "Ford",
    "Nissan",
    "Chevrolet",
    "BMW",
    "Audi",
    "Nissan",
    "Chevrolet",
    "Mercedec-Benz",
    "BMW"
)

old_name = input("Введите название машины для замены: ")
new_name = input("Введите новое название машины: ")

lst_car_name = list(car_name)

lst_car_name = [new_name if x == old_name else x for x in lst_car_name]

car_name = tuple(lst_car_name)

print(car_name)
