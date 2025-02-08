#!/usr/bin/env python3

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from src.classes.stress_bar import *
from src.classes.characters import *
from src.classes.inventory import *
from src.classes.objects import *
from src.classes.menu import *
from src.classes.window import *
from src.classes.room import *
from src.classes.game import Game
from src.credits import *
from random import *

from math import *
import os.path
import pygame
import time

# PLAYER INIT
player = Player("Stellan Voss", pygame.image.load("assets/img/sprite_detective/detective_front.png"), 80, 110, 3, 450, 450, 1, (540, 540))

# ROOMS INIT
rooms = {
    "office": Room(pygame.image.load("assets/img/rooms/office_filled.png"), [], [], 540, 540),
    "carter_house": Room(pygame.image.load("assets/img/background/room1.jpeg"), [], [], 540, 540)
}

# WINDOW INIT
window = Window((1920, 1080), "assets/img/background/room2.jpeg", 30, "You are a Detective and you look for clues because there was a crime and you have to find the culprit")
window.initWindow()
window.setBackground()
window.setFont("assets/font/pixel_font.otf", 42)


# COLOR INIT
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (175, 255, 175)

# MENU INIT
imageStartButton = (
    pygame.image.load("assets/img/Buttons_Pixel_Animation_Pack/play/343px/play01.png"),
    pygame.image.load("assets/img/Buttons_Pixel_Animation_Pack/play/343px/play03.png")
)
imageCreditButton = (
    pygame.image.load("assets/img/Buttons_Pixel_Animation_Pack/about/343px/about01.png"),
    pygame.image.load("assets/img/Buttons_Pixel_Animation_Pack/about/343px/about03.png")
)
imageQuitButton = (
    pygame.image.load("assets/img/Buttons_Pixel_Animation_Pack/back/343px/back01.png"),
    pygame.image.load("assets/img/Buttons_Pixel_Animation_Pack/back/343px/back03.png")
)
startButton = ImageButton(imageStartButton[0], imageStartButton[1], 1920 / 2 - 395, 100, "start")
creditButton = ImageButton(imageCreditButton[0], imageCreditButton[1], 1920 / 2 - 395, 400, "credits")
quitButton = ImageButton(imageQuitButton[0], imageQuitButton[1], 1920 / 2 - 395, 700, "quit")
menu = Menu()
menu.addButton(startButton)
menu.addButton(creditButton)
menu.addButton(quitButton)

# FRUIT INIT
fruits = [
    Item(5, pygame.image.load("assets/img/collect/grapes.png"), (540, 540)),
    Item(5, pygame.image.load("assets/img/collect/pineapple.png"), (540, 540)),
    Item(5, pygame.image.load("assets/img/collect/cherry.png"), (540, 540))
]

#
pygame.mouse.set_visible(False)
stress_bar = StressBar(x=1730, y=220)

# GAME INIT
game = Game(player, rooms, menu, fruits, stress_bar)

# MAIN LOOP
def main():

    first_start = 0
    while window.running:

        game.clock.tick(window.fps)

        frames = window.font.render("fps: " + str(int(game.clock.get_fps())), 1, WHITE)

        # Check events
        for event in pygame.event.get():
            window.checkEvents(event, menu)
            if game.menu.active:
                game.menu.handle_event(event, window)
            elif game.menu.active == False and game.menu.credits == False:
                game.player.move(pygame.key.get_pressed())


        # Print credits
        if game.menu.credits:
            credits(window.screen, game.clock)
            menu.credits = False
            menu.active = True
            menu.activeIndex = 0

        # Print the menu
        elif game.menu.active:
            window.screen.blit(window.backgrnd, (0, 0))
            game.menu.draw(window.screen)
        # The game
        elif not game.menu.active and first_start == 0:
            window.screen.fill(BLACK)
            game.runGame(window.screen)
            stress_bar.start()
            game.startClock()
            first_start = 1

        elif not game.menu.active:
            window.screen.fill(BLACK)
            game.runGame(window.screen)
            stress_bar.update()
            stress_bar.draw(window.screen)

        window.screen.blit(frames, (0, 0))

        window.refresh()

    pygame.quit()
    return

if __name__ == "__main__":
    main()
