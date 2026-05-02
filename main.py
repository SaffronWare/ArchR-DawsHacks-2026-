import pygame
import constants
from draw_functions import *
from bridge_creator import *
from particle import *
from connection import *
from bridge import *

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((constants.window_width, constants.window_height))
surface = pygame.Surface((constants.window_width, constants.window_height))

bg_img = pygame.image.load("assets/gray_city_background.png").convert()


creator = BridgeCreator()


running = True
while running:

    draw_background(surface, bg_img)

    # quit the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    creator.run(pygame.event.get())
    creator.showcase(surface)
    
    

    # draw to objects
    window.blit(surface, (0,0))

    # continuously redraw the screen
    pygame.display.flip()