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
        has_broken=False
        new_particles = []
        broken_connections = []
        for particle in self.particles:
            if particle.anchored and particle not in new_particles:
                new_particles.append(particle)
            particle.update()

        to_remove = []
        
        new_connections = []

        for index, connection in enumerate(self.connections[:]):
            update = connection.update()
            


            if update[0]:
                if connection.reinforced == False:
                    broken_connections.append(index)
                    has_broken =True
                new_particles += update[1:4]
                new_connections += update[4:]

                #new_connections += update[4:]
                pass
            else:
                new_connections.append(connection)
                if connection.p1 not in new_particles:
                    new_particles.append(connection.p1)
                if connection.p2 not in new_particles:
                    new_particles.append(connection.p2)

        self.connections = new_connections
        self.particles = new_particles

        drops = []
        for p in self.particles:
            if getattr(p, 'is_road', False):
                drop = p.original_pos.y - p.pos.y
                drops.append((drop, p.original_index))
        
        drops.sort(key=lambda x: x[0], reverse=True)
        dropped_indices = [idx for drop, idx in drops[:3]]

        return has_broken, broken_connections, dropped_indices
           

    def draw(self, surface : pg.Surface):
        for particle in self.particles:
            particle.draw(surface)
        for connection in self.connections:
            connection.draw(surface)