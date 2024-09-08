"""
Поменяйте местами первый
и последний элемент объекта. Удалите второй элемент. Добавьте в конец ключ «new_key» со
значением «new_value». Выведите на печать итоговый словарь. Важно, чтобы словарь остался
тем же (имел тот же адрес в памяти).
"""
#pylint 10/10
#это наш словарь
my_dict = {"BMW":"E38",
           "fruits":"apple",
           "laptop":"paptop",
           "145":"pikopalpi",
           "Python":"language"}
#это наш оригинальный id
original_id = id(my_dict)
#тут мы меняем местами 1 и 5 значения делаем из нашего словаря список и работаем
keys = list(my_dict.keys())
first_key, last_key = keys[0], keys[-1]
my_dict[first_key],my_dict[last_key] = my_dict[last_key],my_dict[first_key]
#удоляем 2 значение
SECOND_KEY = keys[1]
del my_dict[SECOND_KEY]
#добовляем в конец ключ и значение
my_dict["new_key"] = "new_value"
#свиряем и выводим  я спросил у gpt как сделать вот это условие (имел тот же адрес в памяти). 
assert id(my_dict) == original_id
print(my_dict)
