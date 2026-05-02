from constants import *
import pygame as pg
from pygame import Vector2
from particle import *
from math import exp

class Connection:
    def __init__(self, p1 : Particle, p2 : Particle):
        self.p1 = p1 
        self.p2 = p2
        self.k = 1000
        self.damp = 100
        self.l0 = (p2.pos - p1.pos).length()
    
    def update(self):
        curr_length = (self.p2.pos - self.p1.pos).length()

        norm = (self.p2.pos - self.p1.pos).normalize()
        vel_toward_each_other = (self.p2.velocity - self.p1.velocity).dot(norm)

        diff = self.l0 - curr_length
        force = self.k * diff 

        self.p2.velocity += force * norm * dt 
        self.p1.velocity -= force * norm * dt 

        vel1 = self.p1.velocity.dot(norm) * norm 
        self.p1.velocity -= vel1 

        vel2 = self.p2.velocity.dot(norm) * norm 
        self.p2.velocity -= vel2

        vel1 *= exp(-self.damp * dt)
        vel2 *= exp(-self.damp * dt)
        self.p1.velocity += vel1
        self.p2.velocity += vel2