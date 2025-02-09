import pygame
import time

from src.classes.player import Player
from src.classes.menu import Menu
from src.classes.objects import Item
from src.classes.stress_bar import StressBar

ACTIVE = 1
PASSIVE = 0

class Game():
    def __init__(self, player : Player, rooms, menu : Menu, items : list["Item"], stress : StressBar):
        self.start_time = time.time()
        self.clock = pygame.time.Clock()
        self.actual_room = "hospital"
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
        if (self.cycle == PASSIVE):
            self.cycle = ACTIVE
        else:
            self.cycle = PASSIVE
        return

    def switchRoom(self, new_room : str):
        self.actual_room = new_room
        return

    def runGame(self, screen):
        if self.stress.current_stress < 60:
            self.rooms[self.actual_room].rotation_speed = 1
            self.rooms[self.actual_room].rotation_direction = 1
            self.player.rotation_speed = 1
            self.player.rotation_direction = 1
            if self.rooms[self.actual_room].angle != 0:
                self.rooms[self.actual_room].rotate_back()
            if self.player.angle != 0:
                self.player.rotate_back()
            for item in self.items:
                item.rotation_speed = 1
                item.rotation_direction = 1
                if item.angle != 0:
                    item.rotate_back()
        if 70 <= self.stress.current_stress < 80:
            self.rooms[self.actual_room].rotation_speed = 1
            self.rooms[self.actual_room].rotation_direction = 1
            self.player.rotation_speed = 1
            self.player.rotation_direction = 1
            self.rooms[self.actual_room].rotate()
            self.player.rotate()
            for item in self.items:
                item.rotation_speed = 1
                item.rotation_direction = 1
                item.rotate()
        if 80 <= self.stress.current_stress < 90:
            self.rooms[self.actual_room].rotation_speed = 2
            self.rooms[self.actual_room].rotation_direction = 1
            self.player.rotation_speed = 1.5
            self.player.rotation_direction = 1
            self.rooms[self.actual_room].rotate()
            self.player.rotate()
            for item in self.items:
                item.rotation_speed = 2
                item.rotation_direction = -1
                item.rotate()
        if 90 <= self.stress.current_stress:
            self.rooms[self.actual_room].rotation_speed = 2
            self.rooms[self.actual_room].rotation_direction = -1
            self.player.rotation_speed = 2.25
            self.player.rotation_direction = 1
            self.rooms[self.actual_room].rotate()
            self.player.rotate()
            for item in self.items:
                item.rotation_speed = 1
                item.rotation_direction = -1
                item.rotate()
        self.rooms[self.actual_room].draw(screen)
        for item in self.items:
            item.update(self.stress)
            item.collect(self.player, self.stress)
            item.draw(screen)
        self.player.draw(screen)
        return
