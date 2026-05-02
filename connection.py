from constants import *
import pygame as pg
from pygame import Vector2
from particle import *
from math import exp, tanh
from copy import deepcopy
from draw_functions import draw_rod


def strain_to_color(strain, scale=0.001):


    t = tanh(strain / scale)

    gray = (160, 160, 160)
    red = (255, 60, 60)
    blue = (60, 120, 255)

    if t < 0:
        amount = -t
        return tuple(int(gray[i] * (1 - amount) + red[i] * amount) for i in range(3))
    else:
        amount = t
        return tuple(int(gray[i] * (1 - amount) + blue[i] * amount) for i in range(3))

CONNECTION_TYPES = {
    "STEEL":0,
    "ROAD":1
}

class Connection:
    def __init__(self, p1 : Particle, p2 : Particle):
        self.p1 = p1 
        self.p2 = p2
        self.k = 10000
        self.damp = 2500
        self.l0 = (p2.pos - p1.pos).length()
        self.type = None
        self.strain = 0
        self.broken = False
        
    
    def update(self):
        try:
            curr_length = (self.p2.pos - self.p1.pos).length()

            norm = (self.p2.pos - self.p1.pos).normalize()
            vel_toward_each_other = (self.p2.velocity - self.p1.velocity).dot(norm)
        
            diff = self.l0 - curr_length
            if not self.broken:
                self.strain =  diff / self.l0 * self.k
            else:
                self.strain = 0
            if abs(self.strain) > MAX_STRAIN:
                pass
                dangling1 = deepcopy(self.p1)
                dangling1.should_draw = False
                dangling2 = deepcopy(self.p2)
                dangling2.should_draw = False
                mid = Particle((self.p1.pos + self.p2.pos)/2)
                mid.should_draw = False
                con1 = Connection(dangling1, mid)
                con2 = Connection(dangling2, mid)
                con1.broken = True
                con2.broken = True
                return [True, dangling1, dangling2, mid, con1, con2]
            else:
                force = self.k * diff - self.damp * vel_toward_each_other
                
                self.p1.force_accumulator -= force * norm 
                self.p2.force_accumulator += force * norm
                return [False]
        except Exception as e:
            print(e)
            return [False]


    def draw(self, surface):

        draw_rod(surface, world_to_screen(self.p1.pos), world_to_screen(self.p2.pos), strain_to_color(self.strain))

        