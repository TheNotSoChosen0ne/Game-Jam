#!/usr/bin/env python3

from src.classes.characters import *
from src.classes.inventory import *
from src.classes.objects import *
from src.classes.menu import *
from src.classes.window import *
from src.classes.room import *
from src.classes.game import *
from src.credits import *
from random import *
from math import *
import os.path
import pygame
import time

# PLAYER INIT
player_character = Player("Stellan Voss", None, 0, 0, 0, 540, 540)

# ROOMS INIT
rooms = {
    "office": Room(pygame.image.load("img/empty_room.png"), [], []),
    "carter_house": Room(pygame.image.load("img/room1.jpeg"), [], [])
}

# GAME INIT
game = Game(player_character, rooms)

def main():
    window = Window((1920, 1080), "img/room2.jpeg", 30, "You are a Detective and you look for clues because there was a crime and you have to find the culprit")
    window.initWindow()
    window.setBackground()
    window.setFont("pixel_font.otf", 42)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (175, 255, 175)

    imageStartButton = (
        pygame.image.load("img/Buttons_Pixel_Animation_Pack/play/343px/play01.png"),
        pygame.image.load("img/Buttons_Pixel_Animation_Pack/play/343px/play03.png")
    )
    imageCreditButton = (
        pygame.image.load("img/Buttons_Pixel_Animation_Pack/about/343px/about01.png"),
        pygame.image.load("img/Buttons_Pixel_Animation_Pack/about/343px/about03.png")
    )
    startButton = ImageButton(imageStartButton[0], imageStartButton[1], 1920 / 2, 1080 / 2, "start")
    creditButton = ImageButton(imageCreditButton[0], imageCreditButton[1], 1920 / 2, 1080 / 2 + 200, "credits")
    menu = Menu()
    menu.addButton(startButton)
    menu.addButton(creditButton)

    window.startClock()
    while window.running:

        window.clock.tick(window.fps)

        frames = window.font.render("fps: " + str(int(window.clock.get_fps())), 1, WHITE)
        current = time.time()
        logtime = window.font.render("time: " + str(int(current - window.startTime)), 1, WHITE)

        # Check events
        for event in pygame.event.get():
            window.checkEvents(event)
            if menu.active:
                menu.handle_event(event)

        # Print the menu
        if menu.active:
            window.screen.blit(window.backgrnd, (0, 0))
            menu.draw(window.screen)

        # Print credits
        elif menu.credits:
            credits(window.screen, window.clock)
            menu.credits = False

        # The game
        elif not menu.active:
            window.screen.fill((0, 0, 0)) # Make the screen full black

        window.screen.blit(frames, (0, 0))
        window.screen.blit(logtime, (0, 30))

        window.refresh()

    pygame.quit()
    return

if __name__ == "__main__":
    main()
