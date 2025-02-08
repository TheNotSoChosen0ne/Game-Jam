import pygame
import math

class Player:
    def __init__(self, name: str, spritesheet, frame_width: int, frame_height: int, num_frames: int, 
                 pos_x: int, pos_y: int, delay: int, rotation_center):
        self.name = name
        self.frames = [
            spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            for i in range(num_frames)
        ]
        
        # Position et animation
        self.position = pygame.Vector2(pos_x, pos_y)
        self.index = 0
        self.timer = 0
        self.delay = delay
        self.image = self.frames[self.index]
        
        # Contrôle du mouvement et de l’orientation
        self.speed = 30
        self.angle = 0            # 0° signifie que le joueur regarde vers le haut
        self.rotation_speed = 2
        self.rotation_direction = 1  # 1 pour horaire, -1 pour anti-horaire
        self.rotation_center = pygame.Vector2(rotation_center)  # Centre de rotation (non utilisé pour modifier la position)
    
    def update(self):
        """Met à jour l’animation."""
        self.timer += 1
        if self.timer > self.delay:
            self.timer = 0
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]
    
    def draw(self, screen):
        """Dessine le joueur en tenant compte de sa rotation."""
        rotated_image = pygame.transform.rotate(self.image, -self.angle)
        sprite_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, sprite_rect.topleft)
    
    def move(self, keys):
        """
        Déplace le joueur selon son axe local, qui tourne avec lui.
        
        - UP : avance dans la direction pointée par la tête (forward = (sin(angle), –cos(angle)))
        - DOWN : recule (backward = (–sin(angle), cos(angle)))
        - LEFT : décalage latéral à gauche (strafe gauche = (–cos(angle), –sin(angle)))
        - RIGHT : décalage latéral à droite (strafe droite = (cos(angle), sin(angle)))
        """
        movement = pygame.Vector2(0, 0)
        rad = math.radians(self.angle)
        
        if keys[pygame.K_UP]:
            movement += pygame.Vector2(math.sin(rad), -math.cos(rad)) * self.speed
        
        if keys[pygame.K_DOWN]:
            movement += pygame.Vector2(-math.sin(rad), math.cos(rad)) * self.speed
        
        if keys[pygame.K_LEFT]:
            movement += pygame.Vector2(-math.cos(rad), -math.sin(rad)) * self.speed
        
        if keys[pygame.K_RIGHT]:
            movement += pygame.Vector2(math.cos(rad), math.sin(rad)) * self.speed
        
        self.position += movement
    
    def rotate(self):
        """
        Fait tourner le joueur en continu.
        Ici, on ne modifie que l'angle, afin que les déplacements (move) ne soient pas annulés.
        """
        self.angle = (self.angle + self.rotation_speed * self.rotation_direction) % 360
