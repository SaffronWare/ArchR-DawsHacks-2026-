import pygame as pg
import sys
import constants

pg.init()

window_width = 800
aspect_ratio = 2
window_height = int(window_width / aspect_ratio)

screen = pg.display.set_mode((window_width, window_height))
clock = pg.time.Clock()

bg = (10, 12, 18)
center = (window_width // 2, window_height // 2)
radius = 30


def draw_background(surface):

    surface.fill((15, 20, 25))

    spacing = 30
    grid_color = (30, 35, 40)
    for x in range(0, constants.window_width, spacing):
        pg.draw.line(surface, grid_color, (x, 0), (x, constants.window_height))
    for y in range(0, constants.window_height, spacing):
        pg.draw.line(surface, grid_color, (0, y), (constants.window_width, y))
    
    pg.draw.rect(surface, (10, 15, 20), surface.get_rect(), 15)




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
            radius + i * 1
        )

    pg.draw.circle(surf, color, (cx, cy), radius)

    screen.blit(surf, (x - cx, y - cy))

def draw_rod(surface, start_pos, end_pos, color, width=6):
    """Draw a polished rod with an outline and rounded caps."""
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    # Outline
    outline_color = (25, 25, 25)
    outline_width = width + 2
    outline_radius = outline_width // 2
    pg.draw.line(surface, outline_color, start_pos, end_pos, outline_width)
    pg.draw.circle(surface, outline_color, (int(x1), int(y1)), outline_radius)
    pg.draw.circle(surface, outline_color, (int(x2), int(y2)), outline_radius)
    
    # Main color
    radius = width // 2
    pg.draw.line(surface, color, start_pos, end_pos, width)
    pg.draw.circle(surface, color, (int(x1), int(y1)), radius)
    pg.draw.circle(surface, color, (int(x2), int(y2)), radius)
    
    # Highlight to give it a 3D sheen
    highlight_color = (min(255, color[0] + 70), min(255, color[1] + 70), min(255, color[2] + 70))
    pg.draw.line(surface, highlight_color, start_pos, end_pos, max(1, width // 3))

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