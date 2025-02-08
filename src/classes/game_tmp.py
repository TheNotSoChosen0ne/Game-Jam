from characters import *
import pygame
import time

DAY = 1
NIGHT = 0

class Game:

    def __init__(self, stages, player : Character):
        self.running = True
        self.stages = stages
        self.start = time.time()
        self.font = pygame.font.Font("pixel_font.otf", 42)
        self.player = player
        self.cycle = DAY

    def close_game(self):
        self.running = False

    def get_logtime(self):
        return int(time.time() - self.start)