"""
This module demonstrates the use of power and base in Python.
It assigns values to power, base, and zero variables, prints the type of zero,
creates a result by concatenating the base and power multiplied by zero as strings,
and then prints the type of the result.
"""

POWER = 3
BASE = 2
ZERO = 0

print(type(ZERO))

RESULT = str(BASE) + POWER * str(ZERO)

print(type(RESULT))
