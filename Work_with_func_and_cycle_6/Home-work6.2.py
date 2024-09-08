"""
программу которая будет шифровать текст шифром Цезаря. 
"""

def caeser(text, shift):
    result = []

    for char in text:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(new_char)
    return ''.join(result)

text = input("Введите текст который хотите зашифровать на анг яз: ")
shift = int(input("Введите значение сдвига в циврах: "))
encrypted_text = caeser(text, shift)
print(f"закодирован {encrypted_text}")

decrypted_text = caeser(encrypted_text, -shift)
print(f"раскодирован {decrypted_text}")
