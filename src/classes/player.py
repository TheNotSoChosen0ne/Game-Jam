from src.classes.sprites import *
from src.classes.inventory import *

class Player(Sprite):
    
    def __init__(self, name: str, spritesheet, frame_width: int, frame_height: int, num_frames: int, pos_x: int, pos_y: int, delay : int):
        super().__init__(spritesheet, frame_width, frame_height, num_frames, pos_x, pos_y, delay)
        self.name = name
        self.movable = True
        self.inventory = Inventory()
        self.speed = 30
        return
    
    def draw(self, screen):
        sprite_rect = self.image.get_rect()
        sprite_rect.topleft = (self.position[0], self.position[1] - sprite_rect.height)
        screen.blit(self.image, sprite_rect.topleft)
    
    def move(self, keys):
        """Déplace le personnage selon les touches pressées."""
        if not self.movable:
            return

        x, y = self.position

        if keys[pygame.K_LEFT] and x >= 130:
            x -= self.speed
        if keys[pygame.K_RIGHT] and x <= 400:
            x += self.speed
        if keys[pygame.K_UP] and y >= 250:
            y -= self.speed
        if keys[pygame.K_DOWN] and y <= 920:
            y += self.speed

        self.position = (x, y)
        return
