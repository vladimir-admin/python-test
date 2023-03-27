numbers = [1, 4, 5, 135, 4, 37, 64, 5, 345, 1, 16, 58, 135, 37]
print(numbers)
result = [x for x in numbers if numbers.count(x) == 1]
print(result)