""""
Module to drive car
"""
from shutil import move


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

def follow_roundabout(exit_number):
    """
    Takes the exit number from the roundabout.

    Parameters:
    exit_number (int): The exit number to take from the roundabout.

    Returns:
    None
    """
    print(f'taking exit number {exit_number} from the roundabout')

destination = input("Where do you want to go? ").lower()
start_engine()
move_forward()

if destination=="library":
    turn("left")
    print("we have arrived at the library")
elif destination=="tech park":
    turn("right")
    print("we have arrived at the tech park")
elif destination in ['hospital', 'mall', 'airport', 'university', 'stadium']:
    if destination=='hospital':
        follow_roundabout(1)
        print("we have arrived at the hospital")
    elif destination=='mall':
        follow_roundabout(2)
        move_forward()
        turn("right")
        print("we have arrived at the mall")
    elif destination=='airport':
        follow_roundabout(3)
        print("we have arrived at the airport")
    elif destination in ['university', 'stadium']:
        follow_roundabout(4)
        move_forward()
        if destination=='university':
            turn('left')
            print("we have arrived at the university")
        else:
            turn('right')
            print("we have arrived at the stadium")
else:
    print("destination not found")
stop_engine()