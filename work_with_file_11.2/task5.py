import os
import shutil

# Пути к исходным папкам и к новой папке
source_dirs = ['video', 'sub']
destination_dir = 'watch_me'

# Создание новой папки, если она не существует
os.makedirs(destination_dir, exist_ok=True)

# Перемещение содержимого исходных папок в новую папку
for source_dir in source_dirs:
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        destination_path = os.path.join(destination_dir, item)
        shutil.move(source_path, destination_path)

print(f'Содержимое папок {source_dirs} перемещено в {destination_dir}')