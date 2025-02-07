#!/usr/bin/env python3

from src.characters import *
from src.inventory import *
from src.objects import *
from random import *
from math import *
import pygame
import time

# Initialisation de Pygame
pygame.init()
# Constantes
MENU = "menu_background.jpg"
FRAME_WIDTH = 1920  # Change to match a single frame width
FRAME_HEIGHT = 1200   # Change to match a single frame height
NUM_FRAMES = 30
FPS = 30
# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (175, 255, 175)
# Fenêtre
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("You are a Detective and you look for clues because there was a crime and you have to find the culprit")

backgrnd = pygame.transform.scale(pygame.image.load(MENU), (1920, 1080)) #load un img puis la resize
backgrnd = backgrnd.convert() #convertit en background

# Creation de texte
myfont = pygame.font.Font("pixel_font.otf", 42)
start = time.time()

# Load sprite sheet
#sprite_sheet = pygame.image.load(MENU)

# Boucle principale
running = True
clock = pygame.time.Clock()
#frame = 0

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    frames = myfont.render("fps: " + str(int(clock.get_fps())), 1, WHITE)
    current = time.time()
    logtime = myfont.render("time: " + str(int(current - start)), 1, WHITE)

    # Get the current frame from the sprite sheet
    #frame_x = frame * FRAME_WIDTH  # Calculate x position in sprite sheet
    #frame_surface = sprite_sheet.subsurface((frame_x, 0, FRAME_WIDTH, FRAME_HEIGHT))

    # Draw the frame
    #screen.blit(frame_surface, (0, 0))
    
    # Update frame counter
    #frame = (frame + 1) % NUM_FRAMES  # Loop back to 0 after the last frame

    # Dessiner tout sur l'écran
    screen.blit(backgrnd, (0, 0))
    screen.blit(frames, (0, 0))
    screen.blit(logtime, (0, 30))

    # Rafraîchir l'écran
    pygame.display.flip()

# Quitter
pygame.quit()
