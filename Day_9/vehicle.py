"""
Create a Vehicle class with max_speed and millage instance attributes
"""

class Vehicle:
    def __init__(self, max_speed: float, mileage: float) -> None:
        self.max_speed = max_speed
        self.mileage = mileage

Honda = Vehicle(55, 100)

print(Honda.max_speed, Honda.mileage)