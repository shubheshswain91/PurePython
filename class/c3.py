class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage



class Bus (Vehicle):
   pass


myBus = Bus("Volvo", 180, 12)

print(myBus.name, myBus.max_speed, myBus.mileage)