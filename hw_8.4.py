class Warehouse:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)


class OfficeEquipment:
    def __init__(self, manufacturer, model, price):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, price, max_resolution):
        super().__init__(manufacturer, model, price)
        self.max_resolution = max_resolution


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, price, document_size):
        super().__init__(manufacturer, model, price)
        self.document_size = document_size


class Copier(OfficeEquipment):
    def __init__(self, manufacturer, model, price, max_copy_size):
        super().__init__(manufacturer, model, price)
        self.max_copy_size = max_copy_size


# Пример использования классов
warehouse = Warehouse()

printer = Printer("HP", "Officejet 5255", 120, "4800 x 1200 dpi")
scanner = Scanner("Epson", "Perfection V600", 220, "8.5 x 11.7 in")
copier = Copier("Canon", "imageRUNNER ADVANCE C256iF II", 2400, "11 x 17 in")

warehouse.add_item(printer)
warehouse.add_item(scanner)
warehouse.add_item(copier)

print(len(warehouse.inventory))  # Выведет 3

warehouse.remove_item(scanner)

print(len(warehouse.inventory))  # Выведет 2