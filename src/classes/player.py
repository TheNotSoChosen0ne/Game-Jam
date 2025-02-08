import pygame
import math

class Player:
    def __init__(self, name: str, spritesheet, frame_width: int, frame_height: int, num_frames: int, pos_x: int, pos_y: int, delay: int, scale_factor=5):
        self.name = name
        self.frames = [
            spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            for i in range(num_frames)
        ]
        
        # Agrandissement des frames
        self.frames = [
            pygame.transform.scale(frame, (frame_width * scale_factor, frame_height * scale_factor))
            for frame in self.frames
        ]
        
        # Position, animation et mouvements
        self.position = pygame.Vector2(pos_x, pos_y)
        self.index = 0
        self.timer = 0
        self.delay = delay
        self.image = self.frames[self.index]
        
        # Contrôle du mouvement et de l’orientation
        self.movable = True
        self.speed = 30
        self.angle = 0  # Orientation en degrés
        self.rotation_speed = 2
        self.rotation_direction = -1  # 1 pour horaire, -1 pour anti-horaire

    def update(self):
        """Met à jour l’animation"""
        self.timer += 1
        if self.timer > self.delay:
            self.timer = 0
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]

    def draw(self, screen):
        """Dessine l’entité en tenant compte de sa rotation"""
        rotated_image = pygame.transform.rotate(self.image, -self.angle)
        sprite_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, sprite_rect.topleft)

    def move(self, keys):
        """Déplace l’entité dans la direction de son angle actuel"""
        movement = pygame.Vector2(0, 0)
        rad = math.radians(self.angle)

        if keys[pygame.K_UP]:  # Avancer
            movement.x += math.cos(rad - math.pi / 2) * self.speed
            movement.y += math.sin(rad - math.pi / 2) * self.speed
        
        if keys[pygame.K_DOWN]:  # Reculer
            movement.x += math.cos(rad + math.pi / 2) * self.speed
            movement.y += math.sin(rad + math.pi / 2) * self.speed

        if keys[pygame.K_LEFT]:  # Se déplacer latéralement à gauche
            movement.x -= math.cos(rad) * self.speed
            movement.y -= math.sin(rad) * self.speed
        
        if keys[pygame.K_RIGHT]:  # Se déplacer latéralement à droite
            movement.x += math.cos(rad) * self.speed
            movement.y += math.sin(rad) * self.speed

        self.position += movement

    def rotate(self):
        """Fait tourner l’entité en continu dans le même sens"""
        self.angle = (self.angle + self.rotation_speed * self.rotation_direction) % 360
