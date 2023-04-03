class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass_per_sqm, thickness):
        asphalt_mass = self._length * self._width * mass_per_sqm * thickness
        return asphalt_mass

road = Road(20, 5000)
asphalt_mass = road.asphalt_mass(25, 5)
print(f"The necessary amount of asphalt for the road is {asphalt_mass:.0f} tons.")