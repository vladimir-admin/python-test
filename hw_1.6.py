income = float(input('Ввведите значение выручки: '))
expense = float(input('Ввведите значение издержек фирмы: '))

profit = income - expense

if profit > 0:
    print('Прибыль')
    profitability = profit / income
    print(f'Рентабельность выручки {profitability:.2f}')
    staffCount = int(input('Введите количество сотрдников фирмы: '))
    profitByPerson = profit / staffCount
    print(f'Прибыль в расчете на одного сотрудника {profitByPerson:.2f}')