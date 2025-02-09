#!/usr/bin/env python3

import os
import os.path
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
from src.classes.player import Player
from src.classes.room import Room
from src.classes.window import Window
from src.classes.menu import Menu, ImageButton
from src.classes.music import Music
from src.classes.objects import Item
from src.classes.stress_bar import StressBar
from src.classes.game import Game, ACTIVE, ENDED
from src.credits import credits

# PLAYER INIT
player = Player("Stellan Voss", [pygame.image.load("assets/img/sprite_detective/detective_front.png"),
                                 pygame.image.load("assets/img/sprite_detective/detective_back.png")],
                                80, 110, 2, 450, 450, 1, (540, 540))

# ROOMS INIT
rooms = {
    "hospital": Room(pygame.image.load("assets/img/rooms/hospital.png"), [], [], 540, 540),
    "carter_house": Room(pygame.image.load("assets/img/background/room1.jpeg"), [], [], 540, 540),
    "ending": Room(pygame.image.load("assets/img/rooms/Ending.png"), [], [], 540, 540)
}

# WINDOW INIT
window = Window((1920, 1080), "assets/img/background/room2.jpeg", 30, "Cops Dementia")
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


# PILLS INIT
pills = [
    Item(5, pygame.image.load("assets/img/collect/green_pill.png"), (540, 540), 5, 5, False),
    Item(5, pygame.image.load("assets/img/collect/red_pill.png"), (540, 540), 10, 10, False),
    Item(5, pygame.image.load("assets/img/collect/blue_pill.png"), (540, 540), 25, 0, True),
    Item(5, pygame.image.load("assets/img/collect/yellow_pill.png"), (540, 540), 15, -20, False)
]

# MOUSE
pygame.mouse.set_visible(False)

# STRESS BAR

stress_bar = StressBar(x=1730, y=220)

# GAME INIT
game = Game(player, rooms, menu, pills, stress_bar)


# MAIN LOOP
def main():

    first_start = 0
    menu.music.start_music()
    while window.running:

        game.clock.tick(window.fps)

        frames = window.font.render("fps: " + str(int(game.clock.get_fps())), 1, WHITE)

        # Check events
        for event in pygame.event.get():
            window.checkEvents(event, menu, game)
            if game.menu.active:
                game.menu.handle_event(event, window, game)
            elif game.menu.active == False and game.menu.credits == False:
                game.player.move(pygame.key.get_pressed())


        # Print credits
        if game.menu.credits:
            menu.music.stop_music()
            credits(window.screen, game.clock)
            menu.credits = False
            menu.active = True
            menu.activeIndex = 0
            menu.music.start_music()

        # Print the menu
        elif game.menu.active:
            if not pygame.mixer.music.get_busy():
                menu.music.unpause_music()
            window.screen.blit(window.backgrnd, (0, 0))
            game.menu.draw(window.screen)
            game.start_time += (pygame.time.get_ticks() / 1000)

        elif game.cycle == ACTIVE:
            if first_start == 0:
                menu.music.stop_music()
                game.music.start_music()
                pygame.mixer_music.set_volume(0.5)
                stress_bar.start()
                first_start = 1
            game.runGame(window.screen)
            stress_bar.update()
            stress_bar.draw(window.screen)

        elif game.cycle == ENDED:
            ending(window, game)

        window.screen.blit(frames, (0, 0))

        window.refresh()

    pygame.quit()
    return

if __name__ == "__main__":
    main()
