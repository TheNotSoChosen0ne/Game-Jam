import pygame

class Window():
    def __init__(self, size : tuple, menuPathImage : str, fps : int, gameName : str):
        self.menuPathImage = menuPathImage
        self.gameName = gameName
        self.size = size
        self.fps = fps
        self.fontPath = ""
        self.fontSize = 0
        self.running = True
        self.seconds = 0.0
        return

    def initWindow(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        pygame.display.set_caption(self.gameName)
        return

    def setBackground(self):
        self.backgrnd = pygame.transform.scale(pygame.image.load(self.menuPathImage), (1920, 1080))
        self.backgrnd = self.backgrnd.convert()
        self.screen.fill((0, 0, 0))
        return

    def setFont(self, path : str, size : int):
        self.fontPath = path
        self.fontSize = size
        self.font = pygame.font.Font(self.fontPath, self.fontSize)
        return

    def checkEvents(self, event, menu, game):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if  menu.active == False:
                    game.music.stop_music()
                    menu.music.start_music()
                menu.active = True
        return

    def refresh(self):
        pygame.display.flip()
        return
