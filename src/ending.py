import pygame 
import time
from src.classes.game import Game
from src.classes.window import Window
from src.classes.player import Player
from src.credits import credits

win_screen = pygame.transform.scale(pygame.image.load("assets/img/texts/congrats.jpg"), (1720, 880))
lose_screen = pygame.transform.scale(pygame.image.load("assets/img/texts/lose.jpg"), (1720, 880))

def reach_door(game : Game):
    if game.player.position.distance_to(pygame.Vector2(557, 185)) < 50:
        return True
    return False

def ending(window : Window, game : Game):
    game.switchRoom("ending")
    pygame.mixer.Sound("assets/sfx/ding.mp3").play()
    game.player = Player("Stellan Voss", 80, 110, game.player.position.x, game.player.position.y, 1, (540, 540))
    while not reach_door(game):
        game.clock.tick(window.fps)
        window.screen.fill((0, 0, 0))
        game.rooms[game.actual_room].draw(window.screen)
        pygame.event.get()
        game.player.move(pygame.key.get_pressed())
        game.player.draw(window.screen)
        window.refresh()

    window.screen.fill((0, 0, 0))
    if game.insane == False:
        rect = win_screen.get_rect(center=(window.screen.get_width() // 2, window.screen.get_height() // 2))
        window.screen.blit(win_screen, rect)
    else:
        rect = lose_screen.get_rect(center=(window.screen.get_width() // 2, window.screen.get_height() // 2))
        window.screen.blit(lose_screen, rect)
    window.refresh()
    time.sleep(4)
    window.screen.fill((0, 0, 0))
    window.refresh()
    time.sleep(2)
    credits(window.screen, game.clock)
    pygame.quit()
    exit(0)
