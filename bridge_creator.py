from constants import *
import pygame 
from particle import Particle
from connection import Connection
from bridge import Bridge
from copy import deepcopy

class BridgeCreator:
    @staticmethod
    def generate_generic(self, path):
    
        
        # for now generic algorithm
        particles = deepcopy(path)
        connections = []
        for p1,p2 in zip(particles[:-1], particles[1:]):
            curr_connection = Connection(p1,p2)
            connections.append(curr_connection)
        
        generated_bridge = Bridge()
        generated_bridge.particles = particles
        generated_bridge.connections = connections
        
        return generated_bridge

    def __init__(self):
        self.path = []
        self.roads = []
        self.running = True
    
    def showcase(self, surface):
        self.roads = []
        for particle in self.path:
            particle.draw(surface)
        for p1,p2 in zip(self.particles[:-1], self.particles[1:]):
            road_connection = Connection(p1,p2)
            self.roads.append(road_connection)
            road_connection.draw(surface)


    def run(self, events):
        mouse_pos = pygame.mouse.get_pos()
        curr_particle_pos = screen_to_world(mouse_pos)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    part = Particle(curr_particle_pos)
                    self.path.append(part)
                    


