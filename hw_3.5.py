my_sum = 0
should_continue = True
while should_continue:
    my_str = input('Введите строку чисел, разделенных пробелом, для окончания введите "x": ')
    list_from_str = my_str.split(' ')
    for item in list_from_str:
        if item != 'x':
            my_sum += int(item)
        else:
            should_continue = False
            break
    print(f'Сумма на текущий момент: {my_sum}')
