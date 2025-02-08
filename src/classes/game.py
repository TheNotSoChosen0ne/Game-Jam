import pygame
from typing import List

from src.classes.room import *
from src.classes.player import *
from src.classes.menu import *
from src.classes.window import *

DAY = 1
NIGHT = 0

class Game():
    def __init__(self, player : Player, rooms : List["Room"], menu : Menu):
        self.actual_room = "office"
        self.rooms = rooms
        self.player = player
        self.cycle = DAY
        self.menu = menu
        self.font = pygame.font.Font("assets/font/pixel_font.otf", 42)
        self.time = pygame.time.Clock()
        return

    def switchTime(self):
        if self.cycle == NIGHT:
            self.cycle = DAY
        else:
            self.cycle = NIGHT
        return

    def switchRoom(self, new_room : str):
        self.actual_room = new_room
        return

    def runGame(self, screen):
        self.rooms[self.actual_room].draw(screen)
        self.player.update()
        self.player.draw(screen)
        return
