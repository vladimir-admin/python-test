def int_func(text):
    return text.capitalize()


my_str = input('Введите текст слова разлеленные пробелами:')
print(' '.join(map(int_func, my_str.split(' '))))