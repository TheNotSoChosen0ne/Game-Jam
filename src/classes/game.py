import pygame
import random
from typing import List

from src.classes.room import *
from src.classes.player import *
from src.classes.menu import *
from src.classes.window import *
from src.classes.objects import Item
from src.classes.stress_bar import *

ACTIVE = 1
PASSIVE = 0

class Game():
    def __init__(self, player : Player, rooms : list["Room"], menu : Menu, items : list["Item"], stress : StressBar):
        self.start_time = time.time()
        self.clock = pygame.time.Clock()
        self.actual_room = "office"
        self.rooms = rooms
        self.player = player
        self.cycle = PASSIVE
        self.menu = menu
        self.items = items
        self.stress = stress
        self.font = pygame.font.Font("assets/font/pixel_font.otf", 42)
        return

    def startClock(self):
        self.clock = pygame.time.Clock()
        return

    def switchCycle(self):
        if self.cycle == PASSIVE:
            self.cycle = ACTIVE
        else:
            self.cycle = PASSIVE
        return
    
    def switchRoom(self, new_room : str):
        self.actual_room = new_room
        return

    def runGame(self, screen):
        if (self.cycle == ACTIVE):
            self.rooms[self.actual_room].rotate()
            self.player.rotate()
            for item in self.items:
                item.rotate()
        self.rooms[self.actual_room].draw(screen)
        for item in self.items:
            item.update()
            item.collect(self.player, self.stress)    
            item.draw(screen)
        self.player.draw(screen)
        return

