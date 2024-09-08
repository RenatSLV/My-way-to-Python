def load_file(filename):
    """Чтение данных из файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return ""

def save_file(filename, data):
    """Запись данных в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def main():
    filenames = []
    
    # Ввод названий файлов
    while True:
        filename = input("Введите имя файла (или 'quit' для завершения): ")
        if filename.lower() == 'quit':
            break
        filenames.append(filename)

    if not filenames:
        print("Нет файлов для обработки.")
        return

    # Считывание содержимого файлов и нахождение общих символов
    common_chars = set(load_file(filenames[0]))
    for filename in filenames[1:]:
        file_content = load_file(filename)
        if file_content:
            common_chars &= set(file_content)

    # Преобразование множества символов в строку
    result = ''.join(sorted(common_chars))

    # Запись результата в выходной файл
    output_file = input("Введите имя выходного файла: ")
    save_file(output_file, result)
    print(f"Общие символы сохранены в файл {output_file}")

if __name__ == "__main__":
    main()