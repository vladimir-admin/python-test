n = int(input('Введите целое положительное число: '))
max_digit = 0
while n >= 1:
  last_digit = n % 10
  if last_digit > max_digit:
      max_digit = last_digit
  n = int((n - last_digit) / 10)

print(f'Самая большая цифра: {max_digit}')
