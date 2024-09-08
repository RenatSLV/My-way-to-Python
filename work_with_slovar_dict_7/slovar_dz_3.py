
contry_dict= {}


def add(contry_dict):
    key_to_add = input("Введите страну для добавление: ")
    value_to_add = input("Введите сталицу для добавление : ")
    contry_dict[key_to_add] = value_to_add
    print(contry_dict)

def delet(contry_dict):
    key_to_del = input("Введите страну для удаление: ")
    del contry_dict[key_to_del]
    print(contry_dict)

def find(contry_dict):
    key_to_find = input("Введите страну для поиска: ")
    if key_to_find in contry_dict:
        print(f"эта страна есть в базе {key_to_find}")
        print(contry_dict)
    else:
        print(f"Такой {key_to_find} страны у нас в базе нету")
        print(f"Вот что есть в базе {contry_dict}")
    

def edit(contry_dict):
    key_to_find = input("Введите страну для которую хотите изменить: ")
    if key_to_find in contry_dict:
        new_key = input("Введите новую страну: ")
        new_value = input("Введите новую сталицу: ")
        contry_dict[new_key] = new_value
        print(f"Значение изменины {new_key} {new_value}")
        print(contry_dict)
    else:
        print(f"Такой {key_to_find} страны у нас в базе нету")
        print(f"Вот что есть в базе {contry_dict}")

while True:
    print("Есть такие операции как:\n")
    print("добавление в базу под командой add")
    print("удаление в базе под командой delet")
    print("поиск в базе под командой find")
    print("редактирование в базе под командой edit")
    print("показать базу данных под командой dict")
    operation = input("Выберите операцию над базой: ")
    if operation == "add":
        add(contry_dict)
        print()
    elif operation == "delet":
        delet(contry_dict)
        print()
    elif operation == "find":
        find(contry_dict)
        print()
    elif operation == "edit":
        edit(contry_dict)
        print()
    elif operation == "dict":
        print(contry_dict)
        print()

