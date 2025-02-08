from src.classes.game import Game
from src.classes.sprites import *
from src.classes.game import *
import pygame

class Door(StaticSprite):
    
    def __init__(self, image, pos_x, pos_y, next_room : str):
        super().__init__(image, pos_x, pos_y)
        self.next_room = next_room
        return
    
    def open_door(self, game : Game):
        game.switchRoom(self.next_room)
        return


class Room:
    def __init__(self, sprite, objects, doors, x, y):
        self.sprite = sprite
        self.objects = objects
        self.doors = doors
        self.position = pygame.Vector2(x, y)
        self.angle = 0
        self.rotation_speed = 3
        self.rotation_direction = 1  # Toujours tourner dans le même sens

    def draw(self, screen):
        """Affiche la room avec sa rotation appliquée."""
        rotated_sprite = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated_sprite.get_rect(center=self.position)
        screen.blit(rotated_sprite, rect.topleft)

    def rotate(self):
        """Fait tourner la room en continu dans le même sens."""
        self.angle = (self.angle + self.rotation_speed * self.rotation_direction) % 360
