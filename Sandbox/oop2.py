"""OOP Examples"""
class Person:
    """Person"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        """Introduce person"""
        print(f"Hello, my name is {self.first_name} {self.last_name}")

class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    def introduce(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}, and my employee ID is {self.employee_id}")

person = Person("John", "Doe")
person.introduce()

employee = Employee("Jane", "Smith", 123)
employee.introduce()

# Exercise 2: Inheritance with Constructor
class Shape:
    def __init__(self, color):
        self.color = color

    def description(self):
        print(f"This shape is {self.color}")

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def description(self):
        print(f"This square is {self.color} and has a side length of {self.side_length}")

shape = Shape("red")
shape.description()

square = Square("blue", 4)
square.description()

# Exercise 3: Inheritance and Method Overloading
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def drive(self):
        print("The vehicle is driving")

class Car(Vehicle):
    def __init__(self):
        super().__init__(4)

    def drive(self, speed=None):
        if speed:
            print(f"The car is driving at {speed} mph")
        else:
            print("The car is driving")

vehicle = Vehicle(2)
vehicle.drive()

car = Car()
car.drive()
car.drive(60)

# Exercise 4: Inheritance and Super
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square2(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def perimeter(self):
        return self.width * 4

rectangle = Rectangle(4, 5)
print(f"Rectangle area: {rectangle.area()}")

square = Square2(4)
print(f"Square area: {square.area()}")
print(f"Square perimeter: {square.perimeter()}")