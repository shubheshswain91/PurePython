class Vehicle:
    def __init__(self, maxSpeed, mileage):
        self.max_speed = maxSpeed
        self.mileage = mileage


model = Vehicle(240, 10)

print(model.max_speed, model.mileage)

