"""
программа считает сколько в кортеже встречается даное слово
"""
def count_fruits(fruit_tuple, fruit_name):
    count = 0
    for i in fruit_tuple:
        count += i.lower().count(fruit_name.lower())
    return count

    
fruits = ("banana" ,"apple" ,"bananamango mango" ,"strawberry-banana","orange","grape","pear","lemon","lemon","lemon","grape","grape")
input_text = input("Введите фрукт: ")


print(count_fruits(fruits, input_text))
