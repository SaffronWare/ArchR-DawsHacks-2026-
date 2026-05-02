from constants import *
import pygame as pg
from pygame import Vector2
from particle import *
from math import exp

CONNECTION_TYPES = {
    "STEEL":0,
    "ROAD":1
}

class Connection:
    def __init__(self, p1 : Particle, p2 : Particle):
        self.p1 = p1 
        self.p2 = p2
        self.k = 1000
        self.damp = 100
        self.l0 = (p2.pos - p1.pos).length()
        self.type = None
        self.strain = 0
        
    
    def update(self):
        curr_length = (self.p2.pos - self.p1.pos).length()

        norm = (self.p2.pos - self.p1.pos).normalize()
        vel_toward_each_other = (self.p2.velocity - self.p1.velocity).dot(norm)
     
        diff = self.l0 - curr_length
        self.strain = diff / self.l0
        force = self.k * diff + self.damp * vel_toward_each_other

        self.p2.velocity += force * norm * dt 
        self.p1.velocity -= force * norm * dt 

    def draw(self, surface):
        pg.draw.line(surface, (200,0,200), world_to_screen(self.p1),world_to_screen(self.p2))

        