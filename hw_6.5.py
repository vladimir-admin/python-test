class Stationery:
    title = "Канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашом")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")


# Создание экземпляров классов
s = Stationery()
p = Pen()
pc = Pencil()
h = Handle()

# Вызов метода draw у каждого экземпляра
s.draw()
p.draw()
pc.draw()
h.draw()