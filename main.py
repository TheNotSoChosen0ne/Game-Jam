#!/usr/bin/env python3

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

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
player = Player("Stellan Voss", pygame.image.load("img/sprites/37707_female_front.png"), 16, 32, 1, 100, 250, 1)

# ROOMS INIT
rooms = {
    "office": Room(pygame.image.load("img/empty_dark_room.png"), [], []),
    "carter_house": Room(pygame.image.load("img/room1.jpeg"), [], [])
}

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
imageQuitButton = (
    pygame.image.load("img/Buttons_Pixel_Animation_Pack/back/343px/back01.png"),
    pygame.image.load("img/Buttons_Pixel_Animation_Pack/back/343px/back03.png")
)
startButton = ImageButton(imageStartButton[0], imageStartButton[1], 1920 / 2 - 395, 100, "start")
creditButton = ImageButton(imageCreditButton[0], imageCreditButton[1], 1920 / 2 - 395, 400, "credits")
quitButton = ImageButton(imageQuitButton[0], imageQuitButton[1], 1920 / 2 - 395, 700, "quit")
menu = Menu()
menu.addButton(startButton)
menu.addButton(creditButton)
menu.addButton(quitButton)

# GAME INIT

game = Game(player, rooms, menu)

def main():

    pygame.mouse.set_visible(False)
    window.startClock()
    while window.running:

        window.clock.tick(window.fps)

        frames = window.font.render("fps: " + str(int(window.clock.get_fps())), 1, WHITE)
        current = time.time()
        logtime = window.font.render("time: " + str(int(current - window.startTime)), 1, WHITE)

        # Check events
        for event in pygame.event.get():
            window.checkEvents(event, menu)
            if game.menu.active:
                game.menu.handle_event(event, window)
            elif game.menu.active == False and game.menu.credits == False:
                game.player.move(pygame.key.get_pressed())


        # Print credits
        if game.menu.credits:
            credits(window.screen, window.clock)
            menu.credits = False
            menu.active = True
            menu.activeIndex = 0

        # Print the menu
        elif game.menu.active:
            window.screen.blit(window.backgrnd, (0, 0))
            game.menu.draw(window.screen)

        # The game
        elif not game.menu.active:
            window.screen.fill(BLACK)
            game.runGame(window.screen)

        window.screen.blit(frames, (0, 0))
        window.screen.blit(logtime, (0, 30))

        window.refresh()

    pygame.quit()
    return

if __name__ == "__main__":
    main()
