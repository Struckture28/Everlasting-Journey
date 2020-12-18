from pygame import *
import pygame

from functions import *


config = Game().config

pygame.init()
pygame.display.set_caption(config['GAME_CAPTION'])

screen = pygame.display.set_mode((config['size_x'], config['size_y']))
if config['fullscreen']:
    pygame.display.toggle_fullscreen()

world = World()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
