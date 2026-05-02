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


'''
def draw_glow(screen, center, radius, color):
    x, y = center

    glow_surf = pg.Surface((radius * 6, radius * 6), pg.SRCALPHA)
    # transparent surface so alpha blending works

    cx, cy = radius * 3, radius * 3  # center of glow surface

    # outer glow layers (big + transparent)
    for i in range(12, 0, -1):
        alpha = int(8 * i)  # outer = more transparent
        pg.draw.circle(
            glow_surf,
            (*color, alpha),
            (cx, cy),
            radius + i * 4
        )

    # solid core
    pg.draw.circle(glow_surf, color, (cx, cy), radius)

    # blit onto main screen
    screen.blit(glow_surf, (x - cx, y - cy))'''

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