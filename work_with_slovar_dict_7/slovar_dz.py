"""
Иван решил создать самый большой словарь в мире
"""
#pylint 10/10
my_dict = {"first_one": "we can do it"}

def biggest_dict(**kwargs):
    """
    Эта функция для обновления словаря!
    """
    return my_dict.update(kwargs)

biggest_dict(fruits="apple", kk=123231, pipo="pipo23")
print(my_dict)
