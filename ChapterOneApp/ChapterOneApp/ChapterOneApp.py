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
        print("Total mass is " + str(self.car_mass + (self.pax_count * 70)))

car1 = Car(3, 1600, 5)
car1.total_mass()