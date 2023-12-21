class Car:
    def __init__(self, make, model, year, tires) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.tires = tires

    def start_engine(self):
        print(f"The {self.make} {self.model} {self.year} engine starts.")


my_car = Car("Toyota", "Corolla", 2020, 4)
your_car = Car("Toyota", "Prius", 2019, 6)

my_car.start_engine()
your_car.start_engine()

print(my_car.make)
print(your_car.tires)
