#!/usr/bin/env python3

from src.classes.characters import *
from src.classes.inventory import *
from src.classes.objects import *
from src.classes.menu import *
from src.classes.window import *
from random import *
from math import *
import os.path
import pygame
import time

def main():
    window = Window((1920, 1080), "img/room2.jpeg", 30, "You are a Detective and you look for clues because there was a crime and you have to find the culprit")
    window.initWindow()
    window.setBackground()
    window.setFont("pixel_font.otf", 42)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (175, 255, 175)

    imageStartButton = pygame.image.load("./img/Modern_UI_Pack/Buttons/Normal/Play.png")
    startButton = ImageButton(imageStartButton, 1920 / 2, 1080 / 2)
    menu = Menu([startButton])

    window.startClock()

    while window.running:
        window.checkEvents()

        window.clock.tick(window.fps)

        frames = window.font.render("fps: " + str(int(window.clock.get_fps())), 1, WHITE)
        current = time.time()
        logtime = window.font.render("time: " + str(int(current - window.startTime)), 1, WHITE)

        window.screen.blit(window.backgrnd, (0, 0))
        window.screen.blit(frames, (0, 0))
        window.screen.blit(logtime, (0, 30))

        menu.draw(window.screen)

        window.refresh()

    # Quitter
    pygame.quit()
    return

if __name__ == "__main__":
    main()
