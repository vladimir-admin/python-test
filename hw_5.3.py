filename = 'salaries.txt'
poor_employees = []
total_salary = 0
num_employees = 0

with open(filename, 'r') as f:
    for line in f:
        data = line.strip().split()
        name, salary = data[0], float(data[1])
        total_salary += salary
        num_employees += 1
        if salary < 20000:
            poor_employees.append(name)

print('Сотрудники с окладом менее 20 тысяч:')
for name in poor_employees:
    print(name)

average_salary = total_salary / num_employees
print('Средняя величина дохода сотрудников:', average_salary)