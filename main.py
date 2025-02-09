#!/usr/bin/env python3

import os

from src.classes.player import Player
from src.classes.room import Room
from src.classes.window import Window
from src.classes.menu import Menu, ImageButton
from src.classes.music import Music
from src.classes.objects import Item
from src.classes.stress_bar import StressBar
from src.classes.game import Game
from src.credits import credits

import os.path
import pygame

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# PLAYER INIT
player = Player("Stellan Voss", [pygame.image.load("assets/img/sprite_detective/detective_front.png"),
                                 pygame.image.load("assets/img/sprite_detective/detective_back.png")],
                                80, 110, 2, 450, 450, 1, (540, 540))

# ROOMS INIT
rooms = {
    "hospital": Room(pygame.image.load("assets/img/rooms/hospital.png"), [], [], 540, 540),
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

music_menu = Music("assets/music/MELANCHOLIA.wav")

# FRUIT INIT
fruits = [
    Item(5, pygame.image.load("assets/img/collect/green_pill.png"), (540, 540), 5, 5, False),
    Item(5, pygame.image.load("assets/img/collect/red_pill.png"), (540, 540), 15, 10, False),
    Item(5, pygame.image.load("assets/img/collect/blue_pill.png"), (540, 540), 30, 0, True)
]

# MOUSE
pygame.mouse.set_visible(False)

# STRESS BAR

stress_bar = StressBar(x=1730, y=220)

# GAME INIT
game = Game(player, rooms, menu, fruits, stress_bar)


# MAIN LOOP
def main():

    first_start = 0
    # THEME MENU
    music_menu.start_music()
    #pygame.mixer.music.load("assets/music/menu.mp3")
    #pygame.mixer.music.play(-1)
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
            music_menu.stop_music()
            credits(window.screen, game.clock)
            menu.credits = False
            menu.active = True
            menu.activeIndex = 0
            music_menu.start_music()

        # Print the menu
        elif game.menu.active:
            if not pygame.mixer.music.get_busy():
                music_menu.unpause_music()
            window.screen.blit(window.backgrnd, (0, 0))
            game.menu.draw(window.screen)

        elif not game.menu.active:
            if first_start == 0:
                music_menu.stop_music()
                stress_bar.start()
                first_start = 1
            window.screen.fill(BLACK)
            game.runGame(window.screen)
            stress_bar.update()
            stress_bar.draw(window.screen)
            music_menu.start_music()

        window.screen.blit(frames, (0, 0))

        window.refresh()

    pygame.quit()
    return

if __name__ == "__main__":
    main()
