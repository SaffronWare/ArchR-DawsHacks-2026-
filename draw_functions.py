import pygame as pg
import sys

pg.init()

window_width = 800
aspect_ratio = 2
window_height = int(window_width / aspect_ratio)

screen = pg.display.set_mode((window_width, window_height))
clock = pg.time.Clock()

bg = (10, 12, 18)
center = (window_width // 2, window_height // 2)
radius = 30


def draw_background(surface, bg_img):

    surface.fill((20, 20, 20))

    surface.blit(bg_img, (0, 0))
    # Keep your grid lines if you want them on top:
    spacing = 25
    grid_color_red = 25 # set all rgb values to the same rgb value
    grid_color_green = 25
    grid_color_blue = 25
    for x in range(0, constants.window_width, spacing):
        pg.draw.line(surface, (grid_color_red, grid_color_green, grid_color_blue), (x, 0), (x, constants.window_height))
    for y in range(0, constants.window_height, spacing):
        pg.draw.line(surface, (grid_color_red, grid_color_green, grid_color_blue), (0, y), (constants.window_width, y))




def draw_glow(screen, center, radius, color):
    x, y = center

    size = radius * 10
    surf = pg.Surface((size, size), pg.SRCALPHA)
    cx, cy = size // 2, size // 2

    layers = 14

    for i in range(layers):
        t = i / (layers - 1)  # 0 inner, 1 outer

        # stable falloff with floor so it never disappears
        alpha = int(220 * (1 - t) ** 2.2)
        alpha = max(alpha, 8)  # prevents total disappearance

        pg.draw.circle(
            surf,
            (*color, alpha),
            (cx, cy),
            radius + i * 3
        )

    pg.draw.circle(surf, color, (cx, cy), radius)

    screen.blit(surf, (x - cx, y - cy))

if __name__ == '__main__':
    running=True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False

        screen.fill(bg)
        draw_glow(screen, center, radius, (255, 255, 255))
        pg.display.flip()
        clock.tick(60)

    pg.quit()
    sys.exit()