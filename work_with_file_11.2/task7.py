import os
import shutil

# Имя файла со списком
list_file = 'list.tsv'
# Название новой папки
destination_dir = 'list'

# Создаем новую папку, если она не существует
os.makedirs(destination_dir, exist_ok=True)

# Читаем файл со списком файлов
with open(list_file, 'r') as file:
    files_to_move = file.read().splitlines()

# Перемещаем каждый файл из списка в новую папку
for file_name in files_to_move:
    if os.path.exists(file_name):
        shutil.move(file_name, os.path.join(destination_dir, file_name))

print(f'Файлы из {list_file} перемещены в папку {destination_dir}')