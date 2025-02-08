from src.classes.sprites import *
from src.classes.inventory import *

class Character(Sprite):

    def __init__(self, name: str, spritesheet, frame_width: int, frame_height: int, num_frames: int, pos_x: int, pos_y: int):
        super().__init__(spritesheet, frame_width, frame_height, num_frames, pos_x, pos_y)
        self.name = name
        self.movable = False
        self.inventory = Inventory()
        return
    
    def move(self, keys):
        """Déplace le personnage selon les touches pressées."""
        if not self.movable:
            return

        x, y = self.position

        if keys[pygame.K_LEFT]:
            x -= self.speed
        if keys[pygame.K_RIGHT]:
            x += self.speed
        if keys[pygame.K_UP]:
            y -= self.speed
        if keys[pygame.K_DOWN]:
            y += self.speed

        self.position = (x, y)
        return
