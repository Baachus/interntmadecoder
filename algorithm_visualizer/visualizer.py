''' Visualize algorithms using Pygame '''
import random
import pygame
from algorithm import Algorithm

# Window size
WIDTH = 1800
HEIGHT = 1200

# Bar width and padding
BAR_WIDTH = 5
BAR_PADDING = 2

# Data count
COUNT = WIDTH // (BAR_WIDTH + BAR_PADDING)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 230, 0)

# Initialize Pygame
#pylint: disable=no-member
pygame.init()
#pylint: enable=no-member

win = pygame.display.set_mode((WIDTH, HEIGHT))

# Generate data
data = [random.randint(1, HEIGHT) for _ in range(COUNT)]

def draw(data_to_draw):
    ''' Draw the data '''
    win.fill(BLACK)
    for i, value in enumerate(data_to_draw):
        # Draw a bar for each data point
        pygame.draw.rect(win, GREEN, (i * (BAR_WIDTH + BAR_PADDING), HEIGHT - value, BAR_WIDTH, value))
    pygame.display.update()

def main():
    ''' Main function'''
    # Create the bubble sort generator
    sort_type = input("Press enter sorting method ('bubble', 'merge', 'quick'):")

    if sort_type.lower() == "bubble" or sort_type.lower() == "bubble sort":
        generator = Algorithm.bubble_sort(data)
    elif sort_type == "merge" or sort_type == "merge sort":
        generator = Algorithm.merge_sort(data)
    else:
        generator = Algorithm.quick_sort(data)

    running = True
    while running:
        for event in pygame.event.get():
            #pylint: disable=no-member
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                #pylint: enable=no-member
                return

        try:
            sorted_data = next(generator)
            draw(sorted_data)
        except StopIteration:
            running = False

        pygame.time.delay(10)
    # After sorting is complete, keep the display open until the user closes the window
    while True:
        for event in pygame.event.get():
            #pylint: disable=no-member
            if event.type == pygame.QUIT:
                pygame.quit()
            #pylint: enable=no-member
                return

if __name__ == "__main__":
    main()
