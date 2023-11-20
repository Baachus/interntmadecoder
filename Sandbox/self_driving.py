""""
Module to drive car
"""
def move_forward():
    """
    Moves the vehicle forward.
    """
    print("moving forward")

def turn(direction):
    """
    Turns the vehicle in the specified direction.

    Parameters:
    direction (str): The direction to turn the vehicle. Can be 'left' or 'right'.

    Returns:
    None
    """
    print(f"turning {direction}")

def start_engine():
    """
    Starts the engine of the vehicle.
    """
    print("starting engine")

def stop_engine():
    """
    Stops the engine.
    """
    print("stopping engine")

destination = input("Where do you want to go? ").lower()
start_engine()
move_forward()

if destination=="school":
    turn("left")
    print("we arrived at the school")
elif destination=="grocery store" or destination=="dentist":
    turn("right")
    move_forward()
    if destination=="grocery store":
        turn("right")
        print("we arrived at the grocery store")
    else:
        turn("left")
        print("we arrived at the dentist")
elif destination=="resturant":
    move_forward()
    print("we arrived at the resturant")
else:
    print("destination not found")
