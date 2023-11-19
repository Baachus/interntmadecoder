"""
This program tells you when to take food out of the oven.
"""

TURKEY_COOKING_DURATION = 14
HAM_COOKING_DURATION = 8


def cooking_end_time(start_time, cooking_duration):
    """
    This function calculates the end time of cooking.
    """
    return (start_time + cooking_duration) % 24

print(f"Take the turkey out of the oven at {cooking_end_time(20, TURKEY_COOKING_DURATION)} o'clock")
print(f"Take the ham out of the oven at {cooking_end_time(13, HAM_COOKING_DURATION)} o'clock")
