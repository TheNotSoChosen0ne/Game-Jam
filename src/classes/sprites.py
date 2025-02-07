class Sprites():

    def __init__(self, pos_x, pos_y, x, y, frames, delay):
        self.frames = frames
        self.position = (pos_x, pos_y)
        self.size = (x, y)
        self.delay = delay
        self.index = 0
        self.timer = 0
        self.sprite = self.frames[self.index]
        return self
    
    def update(self):
        self.timer += 1
        if (self.timer > self.delay):
            self.timer = 0
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]

    def draw(self, screen):
        screen.blit(self.image, self.position)
