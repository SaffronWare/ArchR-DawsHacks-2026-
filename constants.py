from pygame import Vector2


# I think for now the units ill use is just SI. So everything
# physics related is in kg, m, m/s, s etc....

# we define useful constants and globals over here
# FOR PYGAME

window_width = 1002
aspect_ratio = 1.5
window_height = int(window_width // aspect_ratio)
fps = 60
dt = 1/fps
sim_speed = 2
dt_sim = dt*sim_speed



world_x_span = 100
world_y_span = world_x_span / aspect_ratio
world_width = 2 * world_x_span
world_height = 2 * world_y_span

def world_to_screen(quantity):
    if isinstance(quantity, Vector2):
        quantity = quantity.copy()
        quantity.y = -quantity.y
        return 0.5 * (quantity + Vector2(world_x_span, world_y_span))/world_x_span * window_width
    elif isinstance(quantity, float) or isinstance(quantity, int):
        return int(0.5 * quantity / world_x_span * window_width)

def screen_to_world(quantity):
    if isinstance(quantity, Vector2):
        quantity = quantity.copy()
        #quantity.y = -quantity.y
        quantity.y = window_height - quantity.y
        lol = 2 * quantity / window_width * world_x_span - Vector2(world_x_span, world_y_span)
        return lol
        return lol
    elif isinstance(quantity, float) or isinstance(quantity, int):
        return 2 * quantity * world_x_span / window_width
    
# FOR PHYSICS
gravity = -9.8
NODE_MASS = 100 # kilograms
NODE_RADIUS=2
START_NODE = (-90, 50)
END_NODE = (90, 50)
MAX_STRAIN = 5
