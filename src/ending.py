import pygame 
import time
from src.classes.game import Game
from src.classes.window import Window
from src.credits import credits
from main import BLACK

end = pygame.image.load("assets/img/.png")

def reach_door(game : Game):
    if game.player.position.distance_to(pygame.Vector2(557, 185)) < 50:
        return True
    return False

def ending(window : Window, game : Game):
    game.switchRoom("ending")
    while not reach_door(game):
        window.screen.fill(BLACK)
        game.rooms[game.actual_room].draw(window.screen)
        game.player.move(pygame.key.get_pressed())
        game.player.draw(window.screen)
    start = time.time()
    while (time.time() - start) >= 3:


    credits(window.screen, game.clock)
