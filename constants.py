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
world_width = 2 * world_x_span
world_height = 2 * world_y_span

def world_to_screen(quantity):
    if isinstance(quantity, Vector2):
        quantity = quantity.copy()
        quantity.y = -quantity.y
        return 0.5 * (quantity + Vector2(world_x_span, world_y_span))/world_x_span * window_width
    elif isinstance(quantity, float):
        return 0.5 * quantity / world_x_span * window_width

def screen_to_world(quantity):
    if isinstance(quantity, Vector2):
        quantity = quantity.copy()
        quantity.y = -quantity.y
        return 2 * quantity / window_width * world_x_span - Vector2(world_x_span, world_y_span)
    elif isinstance(quantity, float):
        return 2 * quantity * world_x_span / window_width