from pygame import Vector2

# we define useful constants and globals over here

window_width = 800
aspect_ratio = 2
window_height = window_width / aspect_ratio
fps = 60
dt = 1/fps
sim_speed = 2
dt_sim = dt*sim_speed

gravity = 9.8
world_x_span = 100
world_y_span = world_x_span / aspect_ratio

def world_to_screen(quantity):
    

def screen_to_world(quantity):

    