import pygame
import time

from src.classes.player import Player
from src.classes.menu import Menu
from src.classes.objects import Item
from src.classes.stress_bar import StressBar
from src.classes.music import Music

ACTIVE = 1
PASSIVE = 0

class Game():
    def __init__(self, player : Player, rooms, menu : Menu, items : list["Item"], stress : StressBar):
        self.start_time = time.time()
        self.clock = pygame.time.Clock()
        self.music = Music("assets/music/game_music.mp3")
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
        if not pygame.mixer.music.get_busy():
            self.music.unpause_music()
        if 65 <= self.stress.current_stress < 75:
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
        if 75 <= self.stress.current_stress < 90:
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
