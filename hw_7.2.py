from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothing):
    def __init__(self, size):
        self._size = size

    @property
    def fabric_consumption(self):
        return self._size / 6.5 + 0.5


class Suit(Clothing):
    def __init__(self, height):
        self._height = height

    @property
    def fabric_consumption(self):
        return 2 * self._height + 0.3


class ClothingFactory:
    @staticmethod
    def create_clothing(clothing_type, param):
        if clothing_type == "coat":
            return Coat(param)
        elif clothing_type == "suit":
            return Suit(param)


items = [
    ClothingFactory.create_clothing("coat", 50),
    ClothingFactory.create_clothing("suit", 165),
    ClothingFactory.create_clothing("coat", 46),
    ClothingFactory.create_clothing("suit", 170)
]

total_fabric_consumption = sum(item.fabric_consumption for item in items)
print(f"Total fabric consumption: {total_fabric_consumption}")