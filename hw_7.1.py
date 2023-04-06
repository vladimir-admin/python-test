class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join([str(item) for item in row]) for row in self.data])

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError('Matrices must be of same size')
        else:
            result = []
            for i in range(len(self.data)):
                result.append([self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))])
            return Matrix(result)