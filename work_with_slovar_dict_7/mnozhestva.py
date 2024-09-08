"""
. Напишите функцию superset(), которая принимает 2 множества. Результат работы 
функции: вывод в консоль одного из сообщений в зависимости от ситуации: 
1 - «Супермножество не обнаружено» 
2 – «Объект {X} является чистым супермножеством» 
3 – «Множества равны»
"""

def superset(set1, set2):
    """
    проверяет множества на условие
    """
    if set1 == set2:
        print("Множества равны")
    elif set1 > set2:
        print(f"Объект {set1} является чистым супермножеством")
    elif set2 > set1:
        print(f"Объект {set2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

#Множества равны
superset({1,2,3}, {1,2,3})

#Объект set1 является чистым супермножеством
superset({1,2,3,4},{1,2,3})

#Объект set2 является чистым супермножеством
superset({1,2},{1,2,3,4})

#Супермножество не обнаружено
superset({1,2,3},{4,5,6})
