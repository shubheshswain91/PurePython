class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def show(self):
        print("The name:{}, maximum speed:{}, mileage: {}  ".format(self.name, self.max_speed, self.mileage))    


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)   ## Inherits the parent class functions with super()

    def showParentAttributes(self):
        return super().show()    


myBus = Bus("School Volvo", 180, 12)

print(myBus.seating_capacity())
myBus.show()

