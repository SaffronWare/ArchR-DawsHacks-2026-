from constants import *
from particle import *
from connection import *
import pygame as pg

class Bridge:
    def __init__(self):
        self.road = []
        self.particles = []
        self.connections = []
    def update(self):
        for particle in self.particles:
            particle.update()
        to_remove = []
        for connection in self.connections:
            update_connection= connection.update()
            if update_connection[0]:
                self.particles += update_connection[1:4]
                for index, connection2 in enumerate(self.connections):
                    if connection.p1 in [connection2.p1, connection2.p2]:
                        to_remove.append(index)
                    elif connection.p2 in [connection2.p1, connection2.p2]:
                        to_remove.append(index)
                try:
                    self.particles.remove(connection.p1)
                except:
                    pass
                try:
                    self.particles.remove(connection.p2)
                except:
                    pass
                try:
                    to_remove.append(self.connections.index(connection))
                except:
                    pass
                try:
                    self.connections += update_connection[4:]
                except:
                    pass
        for index in to_remove:
            self.connections.pop(index)
                
        while None in self.connections:
            self.connections.remove(None)

    def draw(self, surface : pg.Surface):
        for particle in self.particles:
            particle.draw(surface)
        for connection in self.connections:
            connection.draw(surface)