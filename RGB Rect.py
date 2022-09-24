import pygame, colorsys, sys
from pygame.locals import *

FPS = 60
WIDTH, HEIGHT = 500, 500
clock = pygame.time.Clock()
particles = []
particles_E = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
pygame.display.set_caption("RGB Rect")
pygame.event.set_allowed([QUIT])

rgb_temp = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0, 255))
    (r, g, b) = colorsys.hsv_to_rgb(rgb_temp, 1.0, 1.0)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    pygame.draw.rect(screen, (R,G,B), pygame.Rect(200, 200, 100, 100))
    rgb_temp += 0.0001

    pygame.display.flip()
    clock.tick(FPS)
