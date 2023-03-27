# итератор, который повторит элементы списка от 1 до 5, пока не достигнет 13
from itertools import cycle

my_list = [1, 2, 3, 4, 5]
i = 0
for item in cycle(my_list):
    if i > 13:
        break
    print(item)
    i += 1
