class Car:
    """Its a car"""
    def __init__(self,make,model,year,tires,color):
        self.make = make
        self.model = model
        self.year = year
        self.tires = tires
        self.color = color

    def start_car(self):
        """
        Starts the car
        """
        print('Car starting...')

my_car = Car('Toyota', 'Camry', 2020, 4, 'black')
your_car = Car("Toyota", "Prius", 2019, 6, 'red')

my_car.start_car()
your_car.start_car()

print(my_car.make)
print(your_car.tires)
