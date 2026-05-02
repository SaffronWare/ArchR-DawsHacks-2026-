from constants import *
from particle import *
from connection import *
import pygame as pg

class Bridge:
    def __init__(self):
        self.particles = []
        self.connections = []
    def update(self):
        for particle in self.particles:
            particle.update()
        for connection in self.connections:
            connection.update()

    def draw(self, surface : pg.Surface):
        for particle in self.particles:
            particle.draw(surface)
        for connection in self.connections:
            connection.draw(surface)