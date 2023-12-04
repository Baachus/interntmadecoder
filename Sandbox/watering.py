"""
Watering level
"""

WATER_LEVEL = 5

while WATER_LEVEL > 0:
    print(f"Watering plant.  Water level: {WATER_LEVEL}")
    WATER_LEVEL -= 1

for WATER_LEVEL in range(5, 0, -1):
    print(f"Watering plant.  Water level: {WATER_LEVEL}")

lst = [5, 4, 3, 2, 1]

for num in lst:
    print(f"Watering plant.  Water level: {num}")
