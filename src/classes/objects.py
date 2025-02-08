import pygame
import random
from src.classes.player import Player

class Item():

    def __init__(self, points : float, image, center):
        self.points = points
        self.image = image
        self.rotation = 0
        self.speed = 2
        self.pos = pygame.Vector2(random.randint(150, 940), random.randint(200, 890))
        self.center = center
        self.offset = self.pos - self.center
        self.state = "collected"
        return

    def update(self):
        pass

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

    def collect(self, player : Player):
        keys = pygame.key.get_pressed()
        if player.position.distance_to(self.pos) < 100:
            if keys[pygame.K_e]:
                self.state = "collected"
