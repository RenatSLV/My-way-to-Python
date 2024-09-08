import re

def cheak_glas_letter(inp):
    pattern = r'\b[AEIOUaeiouАЕЁИОУЫЭЮЯаеёиоуыэюя]\w*'
    words = re.findall(pattern,inp)
    return words

print("Введите текст:")
inp = input()
print(cheak_glas_letter(inp))

