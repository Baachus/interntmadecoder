"""
This module calculates the areas of different shapes based on user input.
It calculates the area of a rectangle, a circle, and a triangle, and then prints these areas.
"""

import math

def rectangle_area(length, breadth):
    """Calculate the area of a rectangle."""
    return length * breadth

def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius * radius

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def geometry(length, radius):
    """
    Calculate which shape has a larger perimter/circumference and which shape has a larger area.
    """
    square_perimeter = 2 * (length + length)
    circle_circumference = 2 * math.pi * radius
    if square_perimeter > circle_circumference:
        print("The rectangle has a larger perimeter than the circle.")
    elif square_perimeter < circle_circumference:
        print("The circle has a larger circumference than the rectangle.")
    else:
        print("The rectangle and circle have equal perimeters/circumferences.")

    square_area = length * length
    circle_area = math.pi * radius * radius
    if square_area > circle_area:
        print("The rectangle has a larger area than the circle.")
    elif square_area < circle_area:
        print("The circle has a larger area than the rectangle.")
    else:
        print("The rectangle and circle have equal areas.")
    
LENGTH = int(input("Enter the length of the rectangle: "))
BREADTH = int(input("Enter the breadth of the rectangle: "))

print(f"The area of a rectangle with length {LENGTH} and breadth {BREADTH} is: {rectangle_area(LENGTH, BREADTH)}")

RADIUS = int(input("Enter the radius of the circle: "))

print(f"The area of a circle with radius {RADIUS} is: {circle_area(RADIUS)}")

BASE = int(input("Enter the base of the triangle: "))
HEIGHT = int(input("Enter the height of the triangle: "))

print(f"The area of a triangle with base {BASE} and height" +
     " {HEIGHT} is: {triangle_area(BASE, HEIGHT)}")

LENGTH = int(input("Enter the length of the square: "))
RADIUS = int(input("Enter the radius of the circle: "))

geometry(LENGTH, RADIUS)
