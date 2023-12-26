"""Car stuff"""

class Car:
    """Car"""
    def __init__(self, make, model, year, tires) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.tires = tires

    def start_engine(self):
        """Starting engine"""
        print(f"The {self.make} {self.model} {self.year} engine starts.")


class ElectricCar(Car):
    """Electric Car"""
    def __init__(self, make, model, year, tires, battery_life):
        super().__init__(make,model,year,tires)
        self.battery_life = battery_life

    def charge_battery(self):
        """Charging the battery"""
        print('Charging...')


my_car = Car("Toyota", "Corolla", 2020, 4)
your_car = Car("Toyota", "Prius", 2019, 6)

johns_car = ElectricCar("Toyota", "Leaf", 2020, 4, 500)

my_car.start_engine()
# my_car.charge_battery() - will fail as charge_battery is not part of car class

johns_car.start_engine()
johns_car.charge_battery()
