import pygame

class Sprite():

    def __init__(self, spritesheet, frame_width : int, frame_height : int, num_frames : int, pos_x : int, pos_y : int, delay : int):
        self.frames = [
            spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            for i in range(num_frames)
        ]
        scale_factor = 5
        self.frames = [
            pygame.transform.scale(frame, (frame_width * scale_factor, frame_height * scale_factor))
        for frame in self.frames
        ]
        self.position = (pos_x, pos_y)
        self.index = 0
        self.timer = 0
        self.delay = delay
        self.image = self.frames[self.index]

    def update(self):
        self.timer += 1
        if self.timer > self.delay:
            self.timer = 0
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]

    def draw(self, screen):
        screen.blit(self.image, self.position)


class StaticSprite():

    def __init__(self, image, pos_x, pos_y):
        self.image = image
        self.position = (pos_x, pos_y)

    def draw(self, screen):
        screen.blit(self.image, self.position)
