from constants import *
import pygame 
from particle import Particle
from connection import Connection

class BridgeCreator:
    def __init__(self, path, num_rods):
        self.start = path[0]
        self.end = path[1]
        self.roads = path
        
        # for now generic algorithm


