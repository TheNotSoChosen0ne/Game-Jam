import pygame

from src.classes.music import Music

def credits(screen, clock, fps = 30):
    bkgrnd_music = Music("assets/music/credits.mp3")

    original_img = pygame.image.load("assets/img/background/credits.jpg").convert()
    original_img = pygame.transform.scale(original_img, (screen.get_width(), screen.get_height()))
    img = original_img.copy()
    angle = 0

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pygame.font.Font("assets/font/pixel_font.otf", 42)

    credits = [
        "Game Developer:",
        "Lilian Locher",
        "Loann Badina",
        "Corentin Pasquier",
        "Nicolas Bach",
        "Yanis With",
        "Thibaut Musslin (il a juste fait ce système de crédits",
        "mais ne les a pas écrit, donc acte de présence somme toute)",
        "",
        "Art:",
        "Nicolas Bach",
        "Yanis With",
        "",
        "Audio Engineer:",
        "Thibaut Musslin",
        "In addition:",
        "Nicolas Bach",
        "Corentin Pasquier",
        "",
        "Weird Schizophrenia Effects Engineer:",
        "Loann Badina",
        "Loann Badina",
        "Loann Badina",
        "Loann Badina",
        "Loann Badina",
        "Loann Badina",
        "",
        "Yanis With: Bonsoir jeune aventurier, veux-tu faire la quête du forgeron ?",
        "",
        "Special Thanks:",
        "Mr. Guillaumat",
        "Lorem Ipsum",
        "remove.bg",
        "mp3cut.net",
        "piskelapp.com",
        "ytb2mp3.org",
        "resizepixel.com",
    ]

    credit_surfaces = [font.render(line, True, WHITE) for line in credits]
    credit_y = screen.get_height()
    credit_speed = 2
    running = True

    bkgrnd_music.start_music()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BLACK)

        # Rotation
        angle += 1
        img = pygame.transform.rotate(original_img, angle)
        rotated_rect = img.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(img, rotated_rect.topleft)

        # Affichage des crédits
        for i, surface in enumerate(credit_surfaces):
            screen.blit(surface, (screen.get_width() // 2 - surface.get_width() // 2, credit_y + i * 40))

        credit_y -= credit_speed
        if credit_y + len(credit_surfaces) * 40 < 0:
            credit_y = screen.get_height()

        pygame.display.flip()
        clock.tick(fps)

    bkgrnd_music.stop_music()
