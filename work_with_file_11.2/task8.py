# Имя исходного файла
input_file = 'input.txt'
# Имя выходного файла
output_file = 'output.txt'

# Чтение содержимого исходного файла
with open(input_file, 'r') as file:
    lines = file.readlines()

# Удаление последней строки
lines = lines[:-1]

# Запись результата в выходной файл
with open(output_file, 'w') as file:
    file.writelines(lines)

print(f'Последняя строка из файла {input_file} удалена и результат записан в {output_file}')