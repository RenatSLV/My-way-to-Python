import os

# Получаем список всех файлов в текущей директории
files = os.listdir('.')

# Проходим по каждому файлу
for file_name in files:
    # Проверяем, что файл имеет расширение .jpg
    if file_name.endswith('.jpg'):
        # Разделяем имя файла на имя и фамилию
        name, ext = os.path.splitext(file_name)
        parts = name.split('_')
        if len(parts) == 2:
            # Переставляем имя и фамилию местами и создаем новое имя файла
            new_name = f"{parts[1]}_{parts[0]}{ext}"
            # Переименовываем файл
            os.rename(file_name, new_name)

print("Файлы успешно переименованы.")