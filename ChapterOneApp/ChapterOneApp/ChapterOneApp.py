class IllegalCarError (Exception):
    pass

class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

        if pax_count > 5:
            raise IllegalCarError("Too many passangers.")
        elif pax_count < 1:
            raise IllegalCarError("No driver.")

        if self.car_mass + (self.pax_count * 70) > 2000:
            raise IllegalCarError("Exceeded allowed mass with passangers.")

    def total_mass(self):
        print("Total mass is " + str(self.car_mass + (self.pax_count * 70)) + "\n")

print("Chapter One.\n")

while True:
    car = Car(int(input("Provide passangers count: ")), int(input("Provide car mass: ")), int(input("Provide number of gears: ")))
    car.total_mass()