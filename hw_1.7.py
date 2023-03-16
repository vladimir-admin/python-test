a = float(input('Введите сколько километров спортсмен пробежал в первый день: '))
b = float(input('Введите желаемое количество километров: '))

dayNumber = 1
currentDayKm = a
while currentDayKm < b:
    currentDayKm = 1.1*currentDayKm
    dayNumber = dayNumber + 1

print(f'Номер дня: {dayNumber}')