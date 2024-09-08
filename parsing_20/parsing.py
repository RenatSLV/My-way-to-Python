import requests
import os
import json

# URL для загрузки данных
url = "https://jsonplaceholder.typicode.com/posts"

# Создаем папку для хранения файлов, если ее еще нет
output_dir = "json_files_requests"
os.makedirs(output_dir, exist_ok=True)

# Загружаем данные
response = requests.get(url)
data = response.json()

# Сохраняем каждый объект в отдельный файл
for i, item in enumerate(data):
    file_path = os.path.join(output_dir, f"post_{i+1}.json")
    with open(file_path, 'w') as file:
        json.dump(item, file, indent=4)

print(f"Data saved in '{output_dir}' directory.")