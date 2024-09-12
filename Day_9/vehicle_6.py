class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare_charge(self, capacity):
        return capacity * 100


class Bus(Vehicle):

    def seating_capacity(self, capacity):
        super().seating_capacity(capacity)
        return capacity * 100 * 1.1


my_bus = Bus("bus", 30, 50)

print(type(my_bus))
