class MyIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        self.current += 1
        return result