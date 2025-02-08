import pygame
import time

class StressBar:
    def __init__(self, x, y, width=30, height=200, max_stress=100):
        """
        Initializes the stress bar.

        Parameters:
            x (int): X position of the bar.
            y (int): Y position of the bar.
            width (int): Width of the bar.
            height (int): Max height of the bar.
            max_stress (int): Maximum stress value.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_stress = max_stress
        self.current_stress = 0
        self.color = (255, 0, 0)
        self.active = False
        self.last_update_time = 0.0

    def start(self):
        """
        Activates stress increase (should be called when game starts).
        """
        self.active = True
        self.last_update_time = time.time()  # Start the timer

    def update(self):
        """
        Increases stress automatically every second (only if activated).
        """
        if self.active:
            current_time = time.time()
            if current_time - self.last_update_time >= 5:  # timer for the augmentation
                self.current_stress = min(self.max_stress, self.current_stress + 2)  # Increase %
                self.last_update_time = current_time  # Reset timer
                pygame.mixer.init()
                pygame.mixer.music.load("assets/music/stress_bar_sound.mp3")
                pygame.mixer.music.play(0)

    def change_stress(self, change):
        """
        Manually increase or decrease stress.
        Parameters:
            change (float): Positive to increase, negative to decrease.
        """
        self.current_stress = max(0, min(self.max_stress, self.current_stress + change))

    def draw(self, screen):
        """
        Draws the stress bar on the screen.
        Parameters:
            screen (pygame.Surface): The game screen.
        """
        filled_height = (self.current_stress / self.max_stress) * self.height

        # Draw the stress bar (grows upwards)
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y + self.height - filled_height, self.width, filled_height))

        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 3)
