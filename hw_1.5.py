income = float(input('Ввведите значение выручки: '))
expense = float(input('Ввведите значение издержек фирмы: '))

profit = income - expense

if profit > 0:
    print('Прибыль')
else:
    if profit < 0:
        print('Убыток')
    else:
        print('Работает в 0')