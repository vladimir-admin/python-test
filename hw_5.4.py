# coding=utf-8

numbers_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

# открываем файл на чтение
with open('file.txt', 'r') as f:
    lines = f.readlines()

# заменяем английские числительные на русские
rus_lines = []
for line in lines:
    for key, value in numbers_dict.items():
        line = line.replace(key, value)
    rus_lines.append(line)

# записываем новый блок строк в новый файл
with open('new_file.txt', 'w') as f:
    f.writelines(rus_lines)