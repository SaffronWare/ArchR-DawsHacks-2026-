import pygame
import constants
from draw_functions import *
from bridge_creator import *
from particle import *
from connection import *
from bridge import *
import random 
import time
pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((constants.window_width, constants.window_height))
surface = pygame.Surface((constants.window_width, constants.window_height))
# backgrounds = {1: "assets/mountain_landscape16_generated.jpg", 2: "assets/dark_background_dark_blue.jpg", 3: "assets/wallhaven-gwz7ol.png"}
# bg_img = pygame.image.load(random.choice(list(backgrounds.values()))).convert()

bg_img = pygame.image.load("assets/wallhaven-gwz7ol.png").convert()
bg_img = pygame.transform.scale(bg_img, (constants.window_width, constants.window_height))

creator = BridgeCreator()
bridge = None
result_bridge = None

pygame.display.set_caption('ArchR')

BLACK = (50, 50, 50)

class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, BLACK)
 
    def render(self, display):
        self.text = self.font.render(str(round(self.clock.get_fps(),2)), True, BLACK)
        display.blit(self.text, (0, 0))
 
fps = FPS()
prevs = []
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
        result_bridge = deepcopy(bridge)
        creator.showcase(surface)
    else:
        bridge.draw(surface)
        bridge_data = bridge.update()
        if bridge_data[0]:

            for connection_index in bridge_data[1:]:
                connection = result_bridge.connections[connection_index]
                new_point_pos = connection.p1.pos + connection.p2.pos
                new_point_pos /= 2
                new_point = Particle(new_point_pos+Vector2(0,-2))

                result_bridge.particles.append(new_point)
                
                connection_left = Connection(connection.p1, new_point)
                connection_right = Connection(connection.p2, new_point)
                result_bridge.connections += [connection_left, connection_right]
           
            time_after = 0
            while time_after < 2:
                time_after += dt
                draw_background(surface, bg_img)
                bridge.update()
                bridge.draw(surface)
                clock.tick(constants.fps)
                window.blit(surface, (0,0))
                pygame.display.flip()
                prevs.append(deepcopy(bridge))

            for previous_bridge in prevs[::-1]:
                draw_background(surface, bg_img)
                previous_bridge.draw(surface)
                clock.tick(constants.fps)
                window.blit(surface, (0,0))
                pygame.display.flip()
                #time.sleep(1/constants.fps)
            
            bridge = deepcopy(result_bridge)
            prevs = []
        else:
            prevs.append(deepcopy(bridge))

        
    
    # clock.tick()
    # print(clock.get_fps())

    fps.render(surface)
    pygame.display.update()
    fps.clock.tick(0)

    # draw to objects
    window.blit(surface, (0,0))

    # continuously redraw the screen
    pygame.display.flip()
    clock.tick(constants.fps)