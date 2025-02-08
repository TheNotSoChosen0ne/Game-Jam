import pygame

class ImageButton():
    def __init__(self, image, pos_x : float, pos_y : float, type : str):
        self.image = image
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
        self.buttons = []
        self.active = True
        self.credits = False
        return

    def addButton(self, button):
        self.buttons.append(button)
        return

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)
        return

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.imageRect.collidepoint(event.pos):
                    if button.type == "credits":
                        self.credits = True
                    elif button.type == "start":
                        self.active = False
                    return True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if self.buttons[self.activeIndex].type == "start":
                self.active = False
            elif self.buttons[self.activeIndex].type == "credits":
                self.credits = True
            return True
        return False
