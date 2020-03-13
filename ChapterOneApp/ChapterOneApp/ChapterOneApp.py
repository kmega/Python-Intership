class Car:
  def __init__(self, pax_count, car_mass, gear_count):
    self.pax_count = pax_count
    self.car_mass = car_mass
    self.gear_count = gear_count

  def total_mass(self):
    print("Total mass is " + str(self.car_mass + (self.pax_count * 70)))

car1 = Car(3, 1600, 5)

car1.total_mass()
