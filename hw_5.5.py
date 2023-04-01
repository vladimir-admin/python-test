# создаем текстовый файл и записываем в него набор чисел
with open('numbers.txt', 'w') as f:
    f.write('10 20 30 40 50')

# считываем числа из файла и суммируем их
with open('numbers.txt', 'r') as f:
    numbers = f.read().split()
    total = sum(map(int, numbers))

# выводим результат на экран
print('Сумма чисел в файле:', total)