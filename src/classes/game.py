import pygame
import time

from src.color import *
from src.classes.player import Player
from src.classes.menu import Menu
from src.classes.objects import Item
from src.classes.stress_bar import StressBar
from src.classes.music import Music
from src.classes.sprites import StaticSprite

ACTIVE = 1
ENDED = 0

class Game():
    def __init__(self, player : Player, rooms, menu : Menu, items : list["Item"], stress : StressBar):
        self.start_time = time.time()
        self.clock = pygame.time.Clock()
        self.elapsed = 0.0
        self.music = Music("assets/music/game_music.mp3")
        self.actual_room = "hospital"
        self.rooms = rooms
        self.player = player
        self.cycle = ACTIVE
        self.menu = menu
        self.color = (0, 0, 0)
        self.items = items
        self.stress = stress
        self.font = pygame.font.Font("assets/font/pixel_font.otf", 42)
        self.help = StaticSprite(pygame.transform.scale(pygame.image.load("assets/img/collect/legend.png"), (600, 600)), 1200, 200)
        self.has_reached_50 = False
        self.keybinds = StaticSprite(pygame.transform.scale(pygame.image.load("assets/img/collect/keybinds.png"), (900, 900)), 1000, 200)
        return

    def startClock(self):
        self.clock = pygame.time.Clock()
        return

    def switchCycle(self):
        if (self.cycle == ENDED):
            self.cycle = ACTIVE
        else:
            self.cycle = ENDED
        return

    def switchRoom(self, new_room : str):
        self.actual_room = new_room
        return
    
    def win(self):
        self.elapsed += (time.time() - self.start_time)
        self.start_time = time.time()
        if (self.elapsed >= 15): # 203
            return True
        return False

    def runGame(self, screen):
        screen.fill(self.color)
        if not pygame.mixer.music.get_busy():
            self.music.unpause_music()
        if self.win():
            self.switchCycle()
            return
        if self.stress.current_stress >= 50:
            self.has_reached_50 = True
        if not self.has_reached_50:
            self.keybinds.draw(screen)
        if 70 <= self.stress.current_stress < 80:
            self.rooms[self.actual_room].rotation_speed = 1
            self.rooms[self.actual_room].rotation_direction = 1
            self.player.rotation_speed = 1.0
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
            self.color = next_rainbow_color(self.color)
            self.rooms[self.actual_room].rotation_speed = 2.0
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
        if self.has_reached_50:
            self.help.draw(screen)
        self.player.draw(screen)
        return
