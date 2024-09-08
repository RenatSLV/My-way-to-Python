import re

def split_text(inp, delimiters):

    pattern = '|'.join(map(re.escape, delimiters))

    parts = re.split(pattern, inp)

    parts = [part for part in parts if part]
    return parts

print("Введите Текст: ")
inp = input()
delimiters = [' ', ',', '.', ':', ';', '-']

result = split_text(inp, delimiters)
print(result)