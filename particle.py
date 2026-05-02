from pygame import Vector2
import pygame as pg
from constants import *

class Particle:
    def __init__(self, pos=Vector2()):
        self.pos = pos.copy()
        self.radius = NODE_RADIUS
        self.velocity = Vector2()
        self.mass = NODE_MASS
        self.force_accumulator = Vector2()
        self.anchored = False # for now i might add more later

    def update(self):
        if (not self.anchored):
            self.velocity.y += gravity * dt 
            self.velocity +=  self.force_accumulator / self.mass * dt
            self.pos += self.velocity * dt
            self.force_accumulator = Vector2()

    def draw(self, surface: pg.Surface):
        # ok wait first imma draw the actual node
        print(f"radius : {self.radius}")
        pg.draw.circle(surface, (255,255,255), world_to_screen(self.pos), world_to_screen(self.radius))



        # future glow effect after polishing
        # for now nothing
