"""
This module calculates the cost of meals based on the prices of individual items.
It calculates the cost of breakfast, lunch, and dinner, and then prints these costs.
"""

# eggs: $2, banana: $1, salad: $10, steak & rice: $30
# https://realpython.com/python-variables/
# https://www.w3schools.com/python/gloss_python_variable_names.asp

EGGS = 2
BANANA = 1
SALAD = 10
STEAK_AND_RICE = 30

print("breakfast cost: ")
print((EGGS+BANANA))

print("lunch cost: ")
print((SALAD))

print("dinner cost: ")
print((STEAK_AND_RICE + EGGS))
