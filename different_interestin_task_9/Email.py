import re

def cheak_email(inp):
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",inp)
    return emails

print("Введите Email:")
inp = input()
if cheak_email(inp):
    print(inp)
else:
    print("Вводите Email")
    print("На пример Ivan-ivanov1234@mail.kz")