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
        
    

