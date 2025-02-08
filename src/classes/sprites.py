import pygame

class Sprites():

    def __init__(self, spritesheet, frame_rects, pos_x, pos_y, delay):
        self.frames = [spritesheet.subsurface(pygame.Rect(rect)) for rect in frame_rects]
        self.position = (pos_x, pos_y)
        self.delay = delay
        self.index = 0
        self.timer = 0
        self.image = self.frames[self.index]

    def update(self):
        self.timer += 1
        if self.timer > self.delay:
            self.timer = 0
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]

    def draw(self, screen):
        screen.blit(self.image, self.position)
