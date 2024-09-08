def read_file(filename):
    """
    для чтения файла
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не был найден. ")
        return None
    
def write_file(filename, content):
    """
    для записи файла
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def filter_text(input_text, bad_words):
    """
    убирает плохие слова
    """
    words = input_text.split()
    filtered_words = [word for word in words if word.lower() not in bad_words]
    return "".join(filtered_words)

def main():
    
    input_text = read_file("lst.txt")
    if input_text is None:
        return
    
    bad_words_text = read_file("bad_words.txt")
    if bad_words_text is None:
        return
    
    bad_words = set(bad_words_text.lower().split())

    filtered_text = filter_text(input_text, bad_words)

    write_file("output_text.txt", filtered_text)

    read_file("output_text.txt")

if __name__ == "__main__":
    main()