a = int(input('Введите чило a:'))
b = int(input('Введите чило b:'))


def my_division(var_1, var_2):
    if var_2 == 0:
        print('Деление на ноль невозможно!')
    else:
        return var_1 / var_2

print(my_division(a, b))
