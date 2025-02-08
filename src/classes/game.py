import pygame
import random

from src.classes.room import *
from src.classes.player import *
from src.classes.menu import *
from src.classes.window import *
from src.classes.objects import *

DAY = 1
NIGHT = 0

class Game():
    def __init__(self, player : Player, rooms, menu : Menu):
        self.actual_room = "office"
        self.rooms = rooms
        self.player = player
        self.cycle = DAY
        self.menu = menu
        self.font = pygame.font.Font("assets/font/pixel_font.otf", 42)
        self.time = pygame.time.Clock()
        self.fruits = []
        self.fruitsImages = ["assets/img/collect/pineapple.png", "assets/img/collect/grapes.png", "assets/img/collect/cherry.png"]
        self.stress_bar = None
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

    def fillFruits(self):
        while len(self.fruits) != 3:
            index = random.randint(0, 2)
            self.fruits.append(
                Fruits(index + 1, pygame.image.load(self.fruitsImages[index]),
                    (random.randint(200, 890), random.randint(150, 940)), 0, self.player.rotation_center)
            )
        return

    def runGame(self, screen):
        self.fillFruits()
        self.rooms[self.actual_room].rotate()
        self.player.rotate()
        self.rooms[self.actual_room].draw(screen)
        for fruit in self.fruits:
            fruit.rotate()
            if fruit.collect(self.player):
                self.fruits.remove(fruit)
            else:
                fruit.draw(screen)
        self.player.draw(screen)
        return
