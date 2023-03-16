n = int(input('Введите целое положительное число: '))
maxDigit = 0
while n >= 1:
  lastDigit = n % 10
  if lastDigit > maxDigit:
      maxDigit = lastDigit
  n = int((n - lastDigit) / 10)

print(f'Самая большая цифра: {maxDigit}')