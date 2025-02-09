import pygame
from src.classes.music import Music

class ImageButton():
    def __init__(self, imageInactive, imageActive, pos_x : float, pos_y : float, type : str):
        self.imageActive = imageActive
        self.imageInactive = imageInactive
        self.image = self.imageActive
        self.pos = (pos_x, pos_y)
        self.imageRect = self.image.get_rect(topleft=self.pos)
        self.type = type
        return

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        return

class Menu():
    def __init__(self):
        self.activeIndex = 0
        self.music = Music("assets/music/menu.mp3")
        self.buttons = []
        self.active = True
        self.credits = False
        return

    def addButton(self, button):
        self.buttons.append(button)
        return

    def draw(self, screen):
        for i in range(len(self.buttons)):
            if i == self.activeIndex:
                self.buttons[i].image = self.buttons[i].imageActive
            else:
                self.buttons[i].image = self.buttons[i].imageInactive
            self.buttons[i].draw(screen)
        return

    def handle_event(self, event, window, game):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.buttons[self.activeIndex].type == "start":
                    self.active = False
                    self.music.stop_music()
                    game.music.start_music(game.elapsed)
                elif self.buttons[self.activeIndex].type == "credits":
                    self.credits = True
                    self.active = False
                elif self.buttons[self.activeIndex].type == "quit":
                    self.credits = False
                    window.running = False
            if event.key == pygame.K_DOWN:
                self.activeIndex += 1
                if self.activeIndex == len(self.buttons):
                    self.activeIndex = 0
                elif self.activeIndex == -1:
                    self.activeIndex = len(self.buttons) - 1
            if event.key == pygame.K_UP:
                self.activeIndex -= 1
                if self.activeIndex == len(self.buttons):
                    self.activeIndex = 0
                elif self.activeIndex == -1:
                    self.activeIndex = len(self.buttons) - 1
        return
