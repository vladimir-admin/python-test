lst = [1, 4, 5, 135, 4, 37, 64, 5, 345, 1, 16, 58, 135, 37]
result = [x for x in lst if lst.count(x) == 1]
print(result)
