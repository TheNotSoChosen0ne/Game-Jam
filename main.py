from pygame import *

import random
import time
from math import *

# Initialisation de Pygame
init()
# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
FPS = 60
# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (175, 255, 175)
# Fenêtre
screen = display.set_mode(FULLSCREEN)
display.set_caption("You are a Detective and you look for clues because there was a crime and you have to find who did it")

#backgrnd = pygame.transform.scale(pygame.image.load("space.jpg"), (800, 1000)) #load un img puis la resize
#backgrnd = backgrnd.convert() #convertit en background



