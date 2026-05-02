from constants import *
import pygame 
from particle import Particle
from connection import Connection
from bridge import Bridge
from copy import deepcopy

class BridgeCreator:
    @staticmethod
    def generate_generic( path):
    
        
        # for now generic algorithm
        particles = deepcopy(path)
        connections = []
        for p1,p2 in zip(particles[:-1], particles[1:]):
            curr_connection = Connection(p1,p2)
            connections.append(curr_connection)
        
        generated_bridge = Bridge()
        generated_bridge.road = deepcopy(path)
        generated_bridge.particles = particles
        generated_bridge.connections = connections
        
        return generated_bridge

    def __init__(self):
        self.path = [Particle(Vector2(START_NODE)), Particle(Vector2(END_NODE))]
        self.path[0].anchored = True
        self.path[-1].anchored =True
        self.roads = []
        self.running = True
    
    def showcase(self, surface):
        self.roads = []
        for particle in self.path:
            particle.draw(surface)
        for p1,p2 in zip(self.path[:-1], self.path[1:]):
            road_connection = Connection(p1,p2)
            self.roads.append(road_connection)
            road_connection.draw(surface)


    def run(self, events):
        mouse_pos = Vector2(pygame.mouse.get_pos())
        curr_particle_pos = screen_to_world(mouse_pos)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(f"Adding node at {curr_particle_pos}")
                    part = Particle(curr_particle_pos)
                    if self.path[0].pos.x < part.pos.x <  self.path[-1].pos.x:

                        self.path.append(part)
                        self.path = sorted(self.path, key=lambda x: x.pos.x)
                    else:
                        print("Dont even try...")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.running = False 
                    bridge = BridgeCreator.generate_generic(self.path)
                    return bridge
        return None
                    

                    


