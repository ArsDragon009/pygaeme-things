# Imports
import pygame, sys, os

# Main settings
WIDTH = 1100
HEIGHT = 600
FPS = 60

# Init Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modding game")
clock = pygame.time.Clock()
running = True

bgcolor = (0,0,0)

# Import mods
format = ".py" #Здесь вместо ".py" можно поставить любой формат, хоть ".txt"
mods_folder = "mods/" # Можнно изменить также как и формат, но "/" лучше оставить 

for f in os.listdir(mods_folder):
    if f.endswith(format):
        try:
            exec(open(mods_folder+f, encoding = "utf_8").read())
        except Exception as e: print(f"{f} mod error: {e}")

while running:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS) 
    pygame.display.flip()