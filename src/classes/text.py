import pygame

class Text():
    def __init__(self, fontPath : str, size : int, pos : tuple):
        self.fontPath = fontPath
        self.size = size
        self.pos = pos
        return

    def draw(self, text : str, screen, color : tuple):
        self.font = pygame.font.Font(self.fontPath, self.size)
        fontText = self.font.render(text, 1, color)
        screen.blit(fontText, self.pos)
        return
