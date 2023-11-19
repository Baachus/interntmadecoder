"""
This module calculates the areas of different shapes based on user input.
It calculates the area of a rectangle, a circle, and a triangle, and then prints these areas.
"""

import math

LENGTH = int(input("Enter the length of the rectangle: "))
BREADTH = int(input("Enter the breadth of the rectangle: "))

print(f"The area of a rectangle with length {LENGTH} and breadth {BREADTH} is: {LENGTH*BREADTH}")

RADIUS = int(input("Enter the radius of the circle: "))

print(f"The area of a circle with radius {RADIUS} is: {math.pi*RADIUS*RADIUS}")

BASE = int(input("Enter the base of the triangle: "))
HEIGHT = int(input("Enter the height of the triangle: "))

print(f"The area of a triangle with base {BASE} and height {HEIGHT} is: {0.5*BASE*HEIGHT}")
