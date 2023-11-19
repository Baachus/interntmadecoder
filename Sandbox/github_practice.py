"""
This module performs basic arithmetic operations and interacts with the user.
It greets the user, performs addition, subtraction, multiplication, and division 
based on user input, and calculates the user's age on their next birthday.
"""

print("Task 1:")
print("Hello, world!")

greeting = input("What is your name? ")
print(f"Hello, {greeting}")

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} / {number2} = {number1 / number2}")

age = int(input("How old are you? "))
print(f"On your next birthday, you will be {age + 1} years old!")
