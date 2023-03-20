my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число: '))
index = 0
while index < len(my_list) and my_list[index] >= number:
    index += 1

my_list = my_list[:index] + [number] + my_list[index:]
print(my_list)

# number 3
# index 0
# 0 < 5 and 7 >=3
# index 1
# 1 < 5 and 5 >=3
# index 2
# 2 < 5 and 3 >=3
# index 3
# 3 < 5 and 3 >=3
# index 4
# 4 < 5 and 2 >=3
# [7,5,3,3] + [3] + [2]