import pygame
import math

class Player:

    def __init__(self, name: str, frame_width: int, frame_height: int,
                pos_x: int, pos_y: int, delay: int, rotation_center):
        self.name = name
        # Découper les frames du spritesheet
        self.frames = [
            pygame.image.load("assets/img/sprite_detective/detective_back.png").subsurface(pygame.Rect(0, 0, frame_width, frame_height)),
            pygame.image.load("assets/img/sprite_detective/detective_front.png").subsurface(pygame.Rect(0, 0, frame_width, frame_height)),
            pygame.image.load("assets/img/sprite_detective/detective_left.png").subsurface(pygame.Rect(0, 0, frame_width, frame_height)),
            pygame.image.load("assets/img/sprite_detective/detective_right.png").subsurface(pygame.Rect(0, 0, frame_width, frame_height))
        ]

        # Position absolue et calcul de l'offset par rapport au centre de rotation
        self.position = pygame.Vector2(pos_x, pos_y)
        self.rotation_center = pygame.Vector2(rotation_center)
        self.offset = self.position - self.rotation_center  # Vecteur relatif

        # Animation
        self.index = 0
        self.timer = 0
        self.delay = delay
        self.image = self.frames[self.index]

        # Contrôle du mouvement et de l'orientation
        self.speed = 30
        self.angle = 0  # En degrés, 0° signifie que la tête pointe vers le haut
        self.rotation_speed = 2.0
        self.rotation_direction = -1  # 1 pour horaire, -1 pour anti-horaire

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
        Déplace le joueur selon son axe local.
        On suppose que l'angle définit l'orientation du joueur :
          - UP   : avance dans la direction "avant" (local forward = (sin(angle), –cos(angle)))
          - DOWN : recule (local backward = (–sin(angle), cos(angle)))
          - LEFT : décalage latéral à gauche (local left = (–cos(angle), –sin(angle)))
          - RIGHT: décalage latéral à droite (local right = (cos(angle), sin(angle)))
        Après le déplacement, on met à jour l'offset.
        """
        movement = pygame.Vector2(0, 0)
        rad = math.radians(self.angle)

        if keys[pygame.K_UP]:
            if self.position.y + pygame.Vector2(math.sin(rad), -math.cos(rad)).y * self.speed <= 180 or self.position.y + pygame.Vector2(math.sin(rad), -math.cos(rad)).y * self.speed >= 890 or self.position.x + pygame.Vector2(math.sin(rad), -math.cos(rad)).x * self.speed <= 150 or self.position.x + pygame.Vector2(math.sin(rad), -math.cos(rad)).x * self.speed >= 940:
                pass
            else:
                movement += pygame.Vector2(math.sin(rad), -math.cos(rad)) * self.speed
                self.image = self.frames[0]
        if keys[pygame.K_DOWN]:
            if self.position.y + pygame.Vector2(-math.sin(rad), math.cos(rad)).y * self.speed <= 180 or self.position.y + pygame.Vector2(-math.sin(rad), math.cos(rad)).y * self.speed >= 890 or self.position.x + pygame.Vector2(-math.sin(rad), math.cos(rad)).x * self.speed <= 150 or self.position.x + pygame.Vector2(-math.sin(rad), math.cos(rad)).x * self.speed >= 940:
                pass
            else:
                movement += pygame.Vector2(-math.sin(rad), math.cos(rad)) * self.speed
                self.image = self.frames[1]
        if keys[pygame.K_LEFT]:
            if self.position.y + pygame.Vector2(-math.cos(rad), -math.sin(rad)).y * self.speed <= 180 or self.position.y + pygame.Vector2(-math.cos(rad), -math.sin(rad)).y * self.speed >= 890 or self.position.x + pygame.Vector2(-math.cos(rad), -math.sin(rad)).x * self.speed <= 150 or self.position.x + pygame.Vector2(-math.cos(rad), -math.sin(rad)).x * self.speed >= 940:
                pass
            else:
                movement += pygame.Vector2(-math.cos(rad), -math.sin(rad)) * self.speed
                self.image = self.frames[2]
        if keys[pygame.K_RIGHT]:
            if self.position.y + pygame.Vector2(math.cos(rad), math.sin(rad)).y * self.speed <= 180 or self.position.y + pygame.Vector2(math.cos(rad), math.sin(rad)).y * self.speed >= 890 or self.position.x + pygame.Vector2(math.cos(rad), math.sin(rad)).x * self.speed <= 150 or self.position.x + pygame.Vector2(math.cos(rad), math.sin(rad)).x * self.speed >= 940:
                pass
            else:
                movement += pygame.Vector2(math.cos(rad), math.sin(rad)) * self.speed
                self.image = self.frames[3]

        self.position += movement
        # Met à jour l'offset par rapport au centre de rotation
        self.offset = self.position - self.rotation_center

    def rotate(self):
        """
        Fait tourner le joueur autour du centre de rotation.
        La rotation est appliquée en tournant le vecteur offset.
        Si le joueur est déplacé et que l'offset varie, il pourra
        traverser le centre et passer de l'autre côté.
        """
        # Mise à jour de l'angle
        delta_angle = self.rotation_speed * self.rotation_direction
        self.angle = (self.angle + delta_angle) % 360

        # Faire tourner le vecteur offset
        self.offset = self.offset.rotate(delta_angle)
        # Recalcule de la position à partir du centre et du nouvel offset
        self.position = self.rotation_center + self.offset
        self.limits = [self.position.x, self.position.y]

