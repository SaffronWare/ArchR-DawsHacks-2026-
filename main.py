import pygame
import constants

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((constants.window_width, constants.window_height))
surface = pygame.Surface((constants.window_width, constants.window_height))

bg_img = pygame.image.load("assets/gray_city_background.png").convert()

def draw_background(surface, bg_img):

    surface.fill((20, 20, 20))

    surface.blit(bg_img, (0, 0))
    # Keep your grid lines if you want them on top:
    spacing = 25
    grid_color_red = 25 # set all rgb values to the same rgb value
    grid_color_green = 25
    grid_color_blue = 25
    for x in range(0, constants.window_width, spacing):
        pygame.draw.line(surface, (grid_color_red, grid_color_green, grid_color_blue), (x, 0), (x, constants.window_height))
    for y in range(0, constants.window_height, spacing):
        pygame.draw.line(surface, (grid_color_red, grid_color_green, grid_color_blue), (0, y), (constants.window_width, y))

running = True
while running:

    draw_background(surface, bg_img)

    # quit the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # draw to objects
    window.blit(surface, (0,0))

    # continuously redraw the screen
    pygame.display.flip()