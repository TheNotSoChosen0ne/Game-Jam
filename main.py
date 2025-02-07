#!/usr/bin/env python3
import pygame
from random import *
import time
from math import *

# Initialisation de Pygame
pygame.init()
# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
FPS = 60
# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (175, 255, 175)
# Fenêtre
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("You are a Detective and you look for clues because there was a crime and you have to find who did it")

#backgrnd = pygame.transform.scale(pygame.image.load("space.jpg"), (800, 1000)) #load un img puis la resize
#backgrnd = backgrnd.convert() #convertit en background

# Creation du score
#myfont = font.Font("pixel_font.otf", 42)
start = time.time()
# Boucle principale
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Dessiner tout sur l'écran
    #screen.blit(backgrnd, (0, 0))
    #screen.blit(score_display, (600, 950))

    # Rafraîchir l'écran
    pygame.display.flip()

# Quitter
pygame.quit()
