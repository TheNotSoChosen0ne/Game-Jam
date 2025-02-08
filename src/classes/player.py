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
        self.angle = 0            # Orientation en degrés (0° signifie que la tête pointe vers le haut)
        self.rotation_speed = 2
        self.rotation_direction = 1  # 1 pour horaire, -1 pour anti-horaire
        self.rotation_center = pygame.Vector2(rotation_center)  # Centre de rotation fixe

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
        Déplace le joueur selon son axe local (déplacements activables par touches).
        Cette méthode n'est pas modifiée ici.
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
        Fait tourner le joueur autour du centre de rotation fixe.
        À chaque appel, l'angle est mis à jour, puis la position du joueur est recalculée
        pour qu'il orbite autour de `self.rotation_center` en conservant sa distance initiale.
        """
        # Mise à jour de l'angle
        self.angle = (self.angle + self.rotation_speed * self.rotation_direction) % 360

        # Calcul de l'offset entre la position actuelle et le centre de rotation
        offset = self.position - self.rotation_center
        distance = offset.length()

        # Recalcul de la position pour qu'elle soit sur le cercle de rayon "distance" autour du centre,
        # avec le nouvel angle
        rad = math.radians(self.angle)
        self.position.x = self.rotation_center.x + math.cos(rad) * distance
        self.position.y = self.rotation_center.y + math.sin(rad) * distance
