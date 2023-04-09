class Date:
    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def extract_date(cls, date_string):
        day, month, year = map(int, date_string.split("-"))
        return day, month, year

    @staticmethod
    def is_valid_date(day, month, year):
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    def validate(self):
        day, month, year = self.extract_date(self.date_string)
        return self.is_valid_date(day, month, year)

# как пример использования данного кода

date_string = "31-12-2021"
date = Date(date_string)

if date.validate():
    print("Дата валидна")
else:
    print("Дата невалидна")