"""
Задание №1.
"""
TEXT = input("Введите в строку 2 слова: ")

WORD = TEXT.split()
NEW_TEXT = " ".join(WORD[::-1])

print(NEW_TEXT)
