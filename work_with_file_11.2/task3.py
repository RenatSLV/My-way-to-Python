def load_file(filename):
    """Чтение данных из файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

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
        print("Нет файлов для объединения.")
        return

    # Объединение содержимого файлов
    combined_content = ""
    for filename in filenames:
        try:
            combined_content += load_file(filename) + "\n"
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Пропускаем его.")

    # Запись объединенного содержимого в выходной файл
    output_file = input("Введите имя выходного файла: ")
    save_file(output_file, combined_content)
    print(f"Содержимое всех файлов объединено в файл {output_file}")

if __name__ == "__main__":
    main()