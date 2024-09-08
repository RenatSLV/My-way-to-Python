def load_file(filename):
    """Чтение данных из файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def save_file(filename, data):
    """Запись данных в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def transliterate_to_en(text):
    """Транслитерация с русского на английский."""
    ru_to_en = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh',
        'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
        'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts',
        'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
    return ''.join(ru_to_en.get(char, char) for char in text)

def transliterate_to_ru(text):
    """Транслитерация с английского на русский."""
    en_to_ru = {
        'A': 'А', 'B': 'Б', 'V': 'В', 'G': 'Г', 'D': 'Д', 'E': 'Е', 'Zh': 'Ж', 'Z': 'З', 'I': 'И',
        'Y': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П', 'R': 'Р', 'S': 'С',
        'T': 'Т', 'U': 'У', 'F': 'Ф', 'Kh': 'Х', 'Ts': 'Ц', 'Ch': 'Ч', 'Sh': 'Ш', 'Shch': 'Щ', 'Yu': 'Ю',
        'Ya': 'Я', 'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'zh': 'ж', 'z': 'з', 'i': 'и',
        'y': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т',
        'u': 'у', 'f': 'ф', 'kh': 'х', 'ts': 'ц', 'ch': 'ч', 'sh': 'ш', 'shch': 'щ', 'yu': 'ю', 'ya': 'я'
    }
    for en, ru in en_to_ru.items():
        text = text.replace(en, ru)
    return text

def main():
    input_file = input("Введите имя входного файла: ")
    output_file = input("Введите имя выходного файла: ")
    direction = input("Введите направление (1 - с русского на английский, 2 - с английского на русский): ")

    data = load_file(input_file)

    if direction == '1':
        result = transliterate_to_en(data)
    elif direction == '2':
        result = transliterate_to_ru(data)
    else:
        print("Некорректный выбор направления!")
        return

    save_file(output_file, result)
    print(f"Результат сохранен в файл {output_file}")

if __name__ == "__main__":
    main()