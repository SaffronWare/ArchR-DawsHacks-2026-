import pygame
import constants
from draw_functions import *
from bridge_creator import *
from particle import *
from connection import *
from bridge import *
import random 

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((constants.window_width, constants.window_height))
surface = pygame.Surface((constants.window_width, constants.window_height))


backgrounds = {1: "assets/mountain_landscape16_generated.jpg", 2: "assets/dark_background_dark_blue.jpg", 3: "assets/wallhaven-gwz7ol.png"}

# bg_img = pygame.image.load(random.choice(list(backgrounds.values()))).convert()
bg_img = pygame.image.load("assets/wallhaven-gwz7ol.png").convert()
bg_img = pygame.transform.scale(bg_img, (constants.window_width, constants.window_height))

creator = BridgeCreator()
bridge = None

running = True
while running:

    draw_background(surface, bg_img)

    # quit the programe
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False 
    
    if creator.running:
        bridge = creator.run(events)
        creator.showcase(surface)
    else:
        bridge.draw(surface)
        bridge.update()
    

    

    # draw to objects
    window.blit(surface, (0,0))

    # continuously redraw the screen
    pygame.display.flip()