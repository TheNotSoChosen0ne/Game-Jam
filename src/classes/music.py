import pygame

class Music():
    def __init__(self, path_music : str):
        self.path = path_music

    def load_music(self):
        pygame.mixer.music.load(self.path)

    def play_music(self):
        pygame.mixer.music.play(-1) # Boucle infinie (recommence à la fin de la musique)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()
