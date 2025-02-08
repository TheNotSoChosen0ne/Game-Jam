import pygame
from src.classes.player import Player

class Fruit():

    def __init__(self, points : float, image, pos : tuple, rotation : float, center):
        self.points = points
        self.image = image
        self.rotation = rotation
        self.speed = 2
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.center = center
        self.offset = self.pos - self.center
        return

    def update(player : Player):
        pass

    def rotate(self):
        dangle = self.speed
        self.rotation = (self.rotation + dangle) % 360
        self.offset = self.offset.rotate(dangle)
        self.pos = self.center + self.offset
        return

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        sprite_rect = rotated_image.get_rect(center=self.pos)
        screen.blit(rotated_image, sprite_rect.topleft)
        return
