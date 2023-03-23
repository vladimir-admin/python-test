a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
c = int(input('Введите число c:'))


def my_func(param_1, param_2, param_3):
    params_list=[param_1, param_2, param_3]
    params_list.sort()
    return params_list[1] + params_list[2]


print(my_func(a, b, c))
