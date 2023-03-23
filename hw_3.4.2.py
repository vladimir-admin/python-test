# Решение 4 пункта по второму варианту без оператора **

x = float(input('Введите действительное положительное число x:'))
y = int(input('Введите целое отрицательное число y:'))


def my_func(x, y):
    result = 1
    for i in range(y, 0):
        result = result / x

    return result


print(my_func(x, y))
