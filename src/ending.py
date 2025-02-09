import pygame 
import time
from src.classes.game import Game
from src.classes.window import Window
from src.credits import credits

end_screen = pygame.transform.scale(pygame.image.load("assets/img/texts/congrats.jpg"), (1720, 880))

def reach_door(game : Game):
    if game.player.position.distance_to(pygame.Vector2(557, 185)) < 50:
        return True
    return False

def ending(window : Window, game : Game):
    game.switchRoom("ending")
    pygame.mixer.Sound("assets/sfx/ding.mp3").play()
    while not reach_door(game):
        game.clock.tick(window.fps)
        window.screen.fill((0, 0, 0))
        game.rooms[game.actual_room].draw(window.screen)
        pygame.event.get()
        game.player.move(pygame.key.get_pressed())
        game.player.draw(window.screen)
        window.refresh()

    rect = end_screen.get_rect(center=(window.screen.get_width() // 2, window.screen.get_height() // 2))
    window.screen.fill((0, 0, 0))
    window.screen.blit(end_screen, rect)
    window.refresh()
    time.sleep(3)
    credits(window.screen, game.clock)
    pygame.quit()
    exit(0)
