#!/usr/bin/env python3

from src.classes.characters import *
from src.classes.inventory import *
from src.classes.objects import *
from random import *
from math import *
import pygame
import time

# Initialisation de Pygame
pygame.init()
# Constantes
MENU = "img/room2.jpeg"
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

    # Dessiner tout sur l'écran
    screen.blit(backgrnd, (0, 0))
    screen.blit(frames, (0, 0))
    screen.blit(logtime, (0, 30))

    # Rafraîchir l'écran
    pygame.display.flip()

# Quitter
pygame.quit()
