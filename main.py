import pygame
import constants

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((constants.window_width, constants.window_height))
surface = pygame.Surface([constants.window_width, constants.window_height], pygame.SRCALPHA, 32)

def draw_background(window):
    window.fill((255, 0, 0))
    # Keep your grid lines if you want them on top:
    spacing = 60
    for x in range(0, constants.window_width, spacing):
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, constants.window_height))
    for y in range(0, constants.window_height, spacing):
        pygame.draw.line(window, (18, 18, 28), (0, y), (constants.window_width, y))

running = True
while running:
    draw_background(window)

    # press q to quit the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # continuously redraw the screen
    pygame.display.flip()