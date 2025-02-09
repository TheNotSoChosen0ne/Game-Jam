import pygame
import random
from src.classes.stress_bar import StressBar
from src.classes.player import Player

import time
from token import STAR

class Item():

    def __init__(self, points : float, image, center, respawn_time : int, reducer : int, freezing : bool):
        self.points = points
        self.image = pygame.transform.scale(image, (60, 60))
        self.angle = 0
        self.rotation_direction = 1
        self.rotation_speed = 2
        self.pos = pygame.Vector2(random.randint(150, 940), random.randint(200, 890))
        self.center = center
        self.offset = self.pos - self.center
        self.state = "collected"
        self.start_time = 0.0
        self.respawn_time = respawn_time
        self.reducer = reducer
        self.freezing = freezing
        self.spawn_enabled = False # For the spawn of the pill when the stress_bar attain 50% for the first time
        self.freeze_log = True
        return

    def startClock(self):
        self.start_time = time.time()

    def update(self, stress: StressBar):
        elapsed = float(time.time() - self.start_time)

        if stress.current_stress >= 45 and not self.spawn_enabled:
            self.spawn_enabled = True
            self.state = "collected"
            self.startClock()
        elif self.state == "collected" and self.freezing and elapsed > 10 and self.freeze_log:
            stress.freeze(False)
            self.freeze_log = False
        elif self.state == "collected" and self.spawn_enabled and elapsed > self.respawn_time:
            self.state = "spawned"

    def rotate(self):
        dangle = self.rotation_speed * self.rotation_direction
        self.angle = (self.angle + dangle) % 360
        self.offset = self.offset.rotate(dangle)
        self.pos = self.center + self.offset
        return

    def draw(self, screen):
        if self.state != "spawned":
            return
        rotated_image = pygame.transform.rotate(self.image, -self.angle)
        sprite_rect = rotated_image.get_rect(center=self.pos)
        screen.blit(rotated_image, sprite_rect.topleft)
        return

    def randomize(self):
        random.seed(time.time_ns())
        self.pos = pygame.Vector2(random.randint(150, 940), random.randint(200, 890))
        self.offset = self.pos - self.center

    def collect(self, player : Player, stress_bar : StressBar):
        keys = pygame.key.get_pressed()
        if player.position.distance_to(self.pos) < 50 and self.state == "spawned":
            if keys[pygame.K_e]:
                self.state = "collected"
                stress_bar.change_stress(-self.reducer)
                if self.freezing:
                    stress_bar.freeze(True)
                    self.freeze_log = True
                self.randomize()
                self.startClock()
