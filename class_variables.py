class Car:
    wheels = 4
    def __init__(self):
        self.mileage = 10
        self.brand = 'BMW'

c1 = Car()
c2 = Car()

Car.wheels = 5
c1.mileage = 8


print(c1.brand, c1.mileage, c1.wheels)
print(c2.brand, c2.mileage, c2.wheels)