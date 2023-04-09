class Date:
    def __init__(self, date_string):
        self.day, self.month, self.year = map(int, date_string.split('-'))

    def receive_to_warehouse(self, equipment_name, quantity):
        # здесь может быть реализация добавления оргтехники на склад
        print(f'{quantity} единиц оргтехники "{equipment_name}" добавлены на склад')

    def transfer_to_department(self, department_name, equipment_name, quantity):
        # здесь может быть реализация передачи оргтехники в подразделение компании
        print(f'{quantity} единиц оргтехники "{equipment_name}" переданы в подразделение "{department_name}"')