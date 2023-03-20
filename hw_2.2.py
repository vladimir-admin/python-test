my_list = []

while True:
    element = input('Введите значение элемента, для завершения введите "end": ')
    if element == 'end':
        break
    my_list.append(element)

print(f'Введенный список {my_list}')

index = 0
while index < len(my_list) - 1:
    buff = my_list[index+1]
    my_list[index + 1] = my_list[index]
    my_list[index] = buff
    index = index + 2

print(f'Измененный список {my_list}')

# ['1', '2', '3', '4', '5', '6', '7']
# index 0
# 0 < 7 - 1
# ['2', '1', '3', '4', '5', '6', '7']
# index 2
# 2 < 7 - 1
# ['2', '1', '4', '3', '5', '6', '7']
# index 4
# 4 < 7 - 1
# ['2', '1', '4', '3', '6', '5', '7']
# index 6
# 4 < 7 - 1
# 6 < 6