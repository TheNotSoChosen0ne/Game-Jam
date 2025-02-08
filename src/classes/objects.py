import pygame
import random
from src.classes.player import Player
from src.classes.stress_bar import *

class Item():

    def __init__(self, points : float, image, center, respawn_time : int):
        self.points = points
        self.image = image
        self.rotation = 0
        self.speed = 2
        self.pos = pygame.Vector2(random.randint(150, 940), random.randint(200, 890))
        self.center = center
        self.offset = self.pos - self.center
        self.state = "collected"
        self.start_time = 0.0
        self.respawn_time = respawn_time
        return

    def update(self):
        if self.state == "collected" and time.time() - self.start_time > self.respawn_time:
            self.state = "spawned"

    def startClock(self):
        self.start_time = time.time()

    def rotate(self):
        dangle = self.speed
        self.rotation = (self.rotation + dangle) % 360
        self.offset = self.offset.rotate(dangle)
        self.pos = self.center + self.offset
        return

    def draw(self, screen):
        if self.state != "spawned":
            return
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        sprite_rect = rotated_image.get_rect(center=self.pos)
        screen.blit(rotated_image, sprite_rect.topleft)
        return

    def randomize(self):
        pass

    def collect(self, player : Player, stress_bar : StressBar):
        keys = pygame.key.get_pressed()
        if player.position.distance_to(self.pos) < 60 and self.state == "spawned":
            if keys[pygame.K_e]:
                self.state = "collected"
                stress_bar.change_stress(-5)
                self.randomize()
                self.startClock()

