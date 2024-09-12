

class Vehicle:
    def __init__(self, name: str, max_speed: int, mileage: int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, velocity) -> None:
        super().__init__(name, max_speed, mileage)
        self.velocity = velocity
    

Omni_bus = Bus("mazda", 20, 55, 300)

print(Omni_bus.name)
