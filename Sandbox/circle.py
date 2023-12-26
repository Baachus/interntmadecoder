"""A class representing a circle"""

class Circle:
    """A class representing a circle"""
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        """Diameter getter"""
        return self.radius * 2

circle = Circle(5)
print(f"Diameter: {circle.diameter}")

class Person:
    """A class representing a person"""
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        """First name getter"""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value:
            self._first_name = value
        else:
            raise ValueError("First name cannot be empty")

    @property
    def last_name(self):
        """Last name getter"""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value:
            self._last_name = value
        else:
            raise ValueError("Last name cannot be empty")

person = Person("John", "Doe")
print(person.first_name, person.last_name)
person.first_name = "Jane"
person.last_name = "Smith"
print(person.first_name, person.last_name)

class Rectangle:
    """A class representing a rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be a positive number")

    @property
    def height(self):
        """Height getter"""
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be a positive number")

    @property
    def area(self):
        """Area getter"""
        return self._width * self._height

rectangle = Rectangle(4, 5)
print(f"Area: {rectangle.area}")
rectangle.width = 6
rectangle.height = 8
print(f"Area: {rectangle.area}")

class BankAccount:
    """A class representing a bank account"""
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self._balance = initial_balance

    @property
    def balance(self):
        """Balance getter"""
        return self._balance

    def deposit(self, amount):
        """Deposit money into the balance"""
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw money from the balance"""
        self._balance -= amount

    @property
    def is_overdrawn(self):
        """Check if the account is overdrawn"""
        return self._balance < 0

account = BankAccount("123456", 100)
print(f"Initial balance: {account.balance}")

account.deposit(50)
print(f"Balance after deposit: {account.balance}")

account.withdraw(200)
print(f"Balance after withdrawal: {account.balance}")
