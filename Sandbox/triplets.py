"""
This module takes input from the user for three names and a number.
It formats the names by stripping whitespace and capitalizing them, and removes commas from the number.
It then prints the formatted names and the number multiplied by 10.
"""

NAME1 = input("Enter the name of the first person: ")
NAME1_FORMATTED = NAME1.strip().capitalize()
NAME2 = input("Enter the name of the second person: ")
NAME2_FORMATTED = NAME2.strip().capitalize()
NAME3 = input("Enter the name of the third person: ")
NAME3_FORMATTED = NAME3.strip().capitalize()

print(f"The names are: {NAME1_FORMATTED}, {NAME2_FORMATTED}, and {NAME3_FORMATTED}")

X = input("Give me a number to multiply by 10: ").replace(",", "")

print(float(X) * 10)
