class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale.")
        
class Fish(Animal):
    def __init__(self):
        super().__init__() #inherit variables from parent class (Animal)
        
    def breathe(self):
        super().breathe() # inheriting a method
        print("doing this underwater.")
        
    def swim(self):
        print("moving in water.")
        
        
Dog = Fish()
print(Dog.num_eyes)
Dog.breathe()