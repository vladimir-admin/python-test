filename = input("Введите имя файла: ")

with open(filename, 'w') as f:
    while True:
        line = input("Введите строку данных (пустая строка для окончания ввода):\n")
        if line == '':
            break
        f.write(line + '\n')