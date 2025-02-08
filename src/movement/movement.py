import pygame

def handle_movement(keys, position, speed):
    velocity = pygame.math.Vector2(0, 0)

    if keys[pygame.K_UP] == True:
        velocity.y = -speed
    if keys[pygame.K_DOWN] == True:
        velocity.y = speed
    if keys[pygame.K_LEFT] == True:
        velocity.x = -speed
    if keys[pygame.K_RIGHT] == True:
        velocity.x = speed

    position += velocity
    return position
