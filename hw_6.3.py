class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


# Пример использования
worker1 = Position("Иван", "Иванов", "менеджер", 50000, 10000)
print(worker1.name)  # Иван
print(worker1.position)  # менеджер
print(worker1.get_full_name())  # Иван Иванов
print(worker1.get_total_income())  # 60000