a = float(input('Введите сколько километров спортсмен пробежал в первый день: '))
b = float(input('Введите желаемое количество километров: '))

day_number = 1
current_day_km = a
while current_day_km < b:
    current_day_km = 1.1*current_day_km
    day_number = day_number + 1

print(f'Номер дня: {day_number}')