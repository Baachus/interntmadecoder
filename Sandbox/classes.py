class Rectangle:
    """Rectangle"""
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        """returns the area"""
        return self.width*self.height

    def get_perimeter(self):
        """returns the perimeter"""
        return (self.width*2) + (self.height*2)

class Person:
    """Person"""
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        """introduces a Person"""
        print(f'Hello, my name is {self.name}.  I am {self.age} years old and I am {self.gender}')

class Book:
    """Book"""
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_title(self):
        """returns the title"""        
        return self.title

    def get_author(self):
        """returns author"""
        return self.author

    def get_genre(self):
        """returns genre"""
        return self.genre

class Student:
    """Student"""
    def __init__(self,name,age,major,gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def get_name(self):
        """getter for name"""
        return self.name

    def get_age(self):
        """getter for age"""
        return self.age

    def get_major(self):
        """getter for major"""
        return self.major

    def get_gpa(self):
        """getter for GPA"""
        return self.gpa

    def calculate_grade(self):
        """calculates and returns their grade based upon GPA"""
        if self.gpa >= 4.0:
            return "A+"
        elif self.gpa >= 3.7:
            return "A"
        elif self.gpa >= 3.3:
            return "B+"
        elif self.gpa >= 3.0:
            return "B"
        elif self.gpa >= 2.7:
            return "C+"
        elif self.gpa >= 2.3:
            return "C"
        elif self.gpa >= 2.0:
            return "D"
        else:
            return "F"

class Animal:
    """Animal"""
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def get_name(self):
        """getter for name"""
        return self.name

    def get_species(self):
        """getter for species"""
        return self.species

    def eat(self,food):
        """allows the animal to eat the food"""
        print(f"{self.name} is eating {food}")

    def sleep(self):
        """makes the animal sleep"""
        print(f"{self.name} is currently sleeping")

my_rect = Rectangle(100, 20)
print(f"Area of my_rect is {my_rect.get_area()}")
print(f"Perimeter of my_rect is {my_rect.get_perimeter()}")

john = Person("John", 34, "male")
betty = Person("Betty", 42, "female")

john.introduce()
betty.introduce()

the_stand = Book("The Stand", "Steven King", "Horror")

print(f"{the_stand.title} is a {the_stand.genre} book written by {the_stand.author}")

jimmy = Student("Jimmy", 17, "CS", 3.8)

print(f"{jimmy.get_name()} is {jimmy.get_age()} and majoring in {jimmy.get_major()} with a {jimmy.get_gpa()} GPA")
print(f"He currently has a {jimmy.calculate_grade()}")

capybara = Animal('Capybara', 'Rat')


print(f"The {capybara.get_name()} is a {capybara.get_species()} ")
capybara.sleep()
capybara.eat("Strawberries")
