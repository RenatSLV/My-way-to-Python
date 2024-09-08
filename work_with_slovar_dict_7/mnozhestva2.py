englisg_france_slovar = {}

def add(englisg_france_slovar):
    key_to_add = input("введите слово на English: ")
    value_to_add = input("Введите слово на France: ")
    englisg_france_slovar[key_to_add] = value_to_add
    print(englisg_france_slovar)

def delet(englisg_france_slovar):
    key_to_del = input("введите слово на English: ")
    del englisg_france_slovar[key_to_del]
    print(englisg_france_slovar)

def find(englisg_france_slovar):
    key_to_find = input("введите слово на English для поиска: ")
    if key_to_find in englisg_france_slovar:
        print(f"это слово есть в базе {key_to_find}")
        print(englisg_france_slovar)
    else:
        print(f"Такого {key_to_find} слова у нас в базе нету")
        print(f"Вот что есть в базе {englisg_france_slovar}")
    

def edit(englisg_france_slovar):
    key_to_find = input("Введите слово которое хотите изменить: ")
    if key_to_find in englisg_france_slovar:
        new_key = input("Введите новое слово на English: ")
        new_value = input("Введите новое слово на France: ")
        englisg_france_slovar[new_key] = new_value
        print(f"Значение изменины {new_key} {new_value}")
        print(englisg_france_slovar)
    else:
        print(f"Такой {key_to_find} слова у нас в базе нету")
        print(f"Вот что есть в базе {englisg_france_slovar}")

while True:
    print("Есть такие операции как:\n")
    print("добавление в словарь под командой add")
    print("удаление в словаре под командой delet")
    print("поиск в словаре под командой find")
    print("редактирование в словаре под командой edit")
    print("показать словарь под командой dict")

    print()
    operation = input("Выберите операцию над словарём: ")
    print()
    if operation == "add":
        add(englisg_france_slovar)
        print()
    elif operation == "delet":
        delet(englisg_france_slovar)
        print()
    elif operation == "find":
        find(englisg_france_slovar)
        print()
    elif operation == "edit":
        edit(englisg_france_slovar)
        print()
    elif operation == "dict":
        print(englisg_france_slovar)
        print()
    elif operation != "add" "delet" "find" "edit" "dict":
        print("Такой команды у нас нет или вы не правельно ввели команду")
        