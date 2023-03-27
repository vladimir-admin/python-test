def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

n = 5
for el in fact(n):
    print(el)
# выведет факториалы от 1 до 5 (1, 2, 6, 24, 120)