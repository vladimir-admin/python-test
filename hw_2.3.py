season_dic = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
month_number = int(input('Enter month number: '))
for season, numbers in season_dic.items():
    for number in numbers:
        if month_number == number:
            print(season)
