"""
This is the main file for the game.
"""

import pygame
pygame.init()

width, heigh = 800, 600

window = pygame.display.set_mode((width, heigh))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0,0,0))    # Fill window with black
    pygame.display.flip()

pygame.quit()