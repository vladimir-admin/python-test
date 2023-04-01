import json

# создаем и заполняем файл данными о фирмах
with open('firm_data.txt', 'w') as f:
    f.write('firm_1 ООО 10000 5000\n')
    f.write('firm_2 ООО 8000 12000\n')
    f.write('firm_3 ИП 5000 3000\n')
    f.write('firm_4 ЗАО 15000 10000\n')

# читаем файл строка за строкой, вычисляем прибыль и среднюю прибыль
profit_dict = {}
total_profit = 0
count_profit = 0
with open('firm_data.txt') as f:
    for line in f:
        name, form, income, expenses = line.split()
        income = int(income)
        expenses = int(expenses)
        profit = income - expenses
        if profit > 0:
            profit_dict[name] = profit
            total_profit += profit
            count_profit += 1
        else:
            profit_dict[name] = -expenses

if count_profit != 0:
    average_profit = total_profit / count_profit
    average_profit_dict = {"average_profit": average_profit}
else:
    average_profit_dict = {"average_profit": 0}

# сохраняем результаты в виде json-объекта в файл
result_list = [profit_dict, average_profit_dict]
with open('profit_data.json', 'w') as f:
    json.dump(result_list, f)