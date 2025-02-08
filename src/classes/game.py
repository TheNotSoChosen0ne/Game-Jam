import pygame

DAY = 1
NIGHT = 0

class Game():
    def __init__(self, room, player, running : int):
        self.room = room
        self.rooms = []
        self.player = player
        self.running = running
        self.cycle = DAY
        self.font = pygame.font.Font("pixel_font.otf", 42)
        self.time = pygame.time.Clock()
        return

    def switchTime(self):
        if self.cycle == NIGHT:
            self.cycle = DAY
        else:
            self.cycle = NIGHT
        return
