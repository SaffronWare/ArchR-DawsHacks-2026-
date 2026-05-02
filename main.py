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
creator = BridgeCreator()
bridge = None
result_bridge = None

pygame.display.set_caption('ArchR')

BLACK = (50, 50, 50)

class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20, bold=True)
        self.color = (200, 220, 240)
 
    def render(self, display):
        self.text = self.font.render(f"FPS: {round(self.clock.get_fps())}", True, self.color)
        display.blit(self.text, (20, 20))

def reinforce_bridge(indeces, above=False):
    for connection_index in indeces:
                connection = result_bridge.connections[connection_index]
                
                new_point_pos = connection.p1.pos + connection.p2.pos
                new_point_pos /= 2
         
                new_point = Particle(new_point_pos+Vector2(0,-8 if not above else 8))

                x_neighbours = list(sorted(result_bridge.particles, key=lambda x: abs(x.pos.x-new_point.pos.x)))[:10]

                for neighbor in x_neighbours:
                     if abs(neighbor.pos.y - new_point.pos.y) < 0.5 and (neighbor.pos - new_point.pos).length() > 0.1:
                          result_bridge.connections.append(Connection(new_point, neighbor))
                          break


                result_bridge.particles.append(new_point)
                    
                connection_left = Connection(connection.p1, new_point)
                connection_right = Connection(connection.p2, new_point)
                result_bridge.connections += [connection_left, connection_right]

                

 
fps = FPS()
prevs = []
running = True
while running:

    draw_background(surface)

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
        has_broken, broken_connections, dropped_indices = bridge.update()
        if has_broken:

            reinforce_bridge(broken_connections + dropped_indices, True)
           
            time_after = 0
            while time_after < 2:
                time_after += dt
                draw_background(surface)
                bridge.update()
                bridge.draw(surface)
                clock.tick(constants.fps)
                window.blit(surface, (0,0))
                pygame.display.flip()
                prevs.append(deepcopy(bridge))

            for previous_bridge in prevs[::-1]:
                draw_background(surface)
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