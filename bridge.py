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

        drops = []
        for p in self.particles:
            if getattr(p, 'is_road', False):
                drop = p.original_pos.y - p.pos.y
                drops.append((drop, p))
        
        drops.sort(key=lambda x: x[0], reverse=True)
        dropped_particles = [p for drop, p in drops[:3] if drop > 0]

        dropped_connection_indices = []
        for index, connection in enumerate(self.connections):
            if connection.p1 in dropped_particles or connection.p2 in dropped_particles:
                dropped_connection_indices.append(index)

        self.connections = new_connections
        self.particles = new_particles

        return has_broken, broken_connections, dropped_connection_indices
           

    def draw(self, surface : pg.Surface):
        for particle in self.particles:
            particle.draw(surface)
        for connection in self.connections:
            connection.draw(surface)