from pygame import Vector2
import pygame as pg
from constants import *

class Particle:
    def __init__(self, pos=Vector2(), radius=0):
        self.pos = pos.copy()
        self.radius = radius
        self.velocity = Vector2()
        self.mass = NODE_MASS
        self.force_accumulator = Vector2()
        self.anchored = False # for now i might add more later

    def update(self):
        self.velocity.y += gravity * dt
        self.pos += self.velocity * dt
        self.force_accumulator = Vector2()

    def draw(self, surface: pg.Surface):
        # ok wait first imma draw the actual node
        pg.draw.circle(surface, (255,255,255), world_to_screen(self.pos), world_to_screen(self.radius))



        # future glow effect after polishing
        # for now nothing
