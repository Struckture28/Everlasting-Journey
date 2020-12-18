import pygame

from functions import *
from config import *


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(GAME_CAPTION)

    screen = pygame.display.set_mode((size_x, size_y))
    if fullscreen:
        pygame.display.toggle_fullscreen()

    print()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()
