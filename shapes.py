import math

length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

print(f"The area of a rectangle with length {length} and breadth {breadth} is: {length*breadth}")

radius = int(input("Enter the radius of the circle: "))

print(f"The area of a circle with radius {radius} is: {math.pi*radius*radius}")

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))

print(f"The area of a triangle with base {base} and height {height} is: {0.5*base*height}")
