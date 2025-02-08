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


class Room():
    
    def __init__(self, sprite, objects, doors):
        self.sprite = sprite
        self.objects = objects
        self.doors = doors
        return
    
    def draw(self, screen):
        screen.blit(self.sprite, (0, 0))
