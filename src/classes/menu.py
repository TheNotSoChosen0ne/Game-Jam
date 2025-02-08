import pygame

class ImageButton():
    def __init__(self, image, pos_x : float, pos_y : float, callback):
        self.image = image
        self.pos = (pos_x, pos_y)
        self.callback = callback
        self.selected = False
        return

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        return

    def click(self):
        self.callback()
        return

class Menu():
    def __init__(self, buttons : list):
        self.buttons = buttons
        self.selected_index = 0
        self.buttons[self.selected_index].selected = True
        return

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)
        return

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.buttons[self.selected_index].selected = False
                self.selected_index = (self.selected_index + 1) % len(self.buttons)
                self.buttons[self.selected_index].selected = True
            elif event.key == pygame.K_UP:
                self.buttons[self.selected_index].selected = False
                self.selected_index = (self.selected_index - 1) % len(self.buttons)
                self.buttons[self.selected_index].selected = True
            elif event.key == pygame.K_RETURN:
                self.buttons[self.selected_index].click()
        return
