class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    ...

class Car(Vehicle):
    ...
    
school_bus = Bus("Volvo", 180, 12)
print(school_bus.color, school_bus.name, "Speed: ", school_bus.max_speed, "Mileage: ", school_bus.mileage)


car = Car("Audi", 240, 20)
print(car.color, car.name, "Speed: ", car.max_speed, "Mileage: ", car.mileage)
