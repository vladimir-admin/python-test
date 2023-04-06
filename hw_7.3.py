class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            return "Невозможно выполнить операцию"

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, row_len):
        rows = self.cells // row_len
        remainder = self.cells % row_len
        result = ""
        for i in range(rows):
            result += "*" * row_len + "\n"
        result += "*" * remainder
        return result


cell1 = Cell(12)
cell2 = Cell(5)

print((cell1 + cell2).cells)  # 17
print((cell1 - cell2).cells)  # 7
print((cell1 * cell2).cells)  # 60
print((cell1 / cell2).cells)  # 2

print(cell1.make_order(5))
