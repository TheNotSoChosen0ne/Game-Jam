import pygame

def credits(screen, clock, fps=30):
    pygame.mixer.init()
    pygame.mixer.music.load("music/credits.mp3")
    pygame.mixer.music.play()
    img = pygame.image.load("img/credits.jpg").convert()
    img = pygame.transform.scale(img, (screen.get_width(), screen.get_height()))
    img.set_alpha(200)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pygame.font.Font("pixel_font.otf", 42)
    credits = [
        "Script: Loann Badina",
        "Art: Nicolas Bach",
        "Game Developer: Lilian Locher",
        "Audio Engineer: Thibaut Musslin",
        "",
        "Yanis With: Bonsoir jeune aventurier, veux-tu faire la quête du forgeron ?",
        "",
        "Special Thanks: Mr. Guillaumat",
        "Special Thanks: Fab",
        "Special Thanks: Lorem Ipsum",
    ]

    credit_surfaces = [font.render(line, True, WHITE) for line in credits]
    credit_y = screen.get_height()
    credit_speed = 2
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill(BLACK)
        screen.blit(img, (screen.get_width() // 2 - img.get_width() // 2, screen.get_height() // 2 - img.get_height() // 2))
        img = pygame.transform.rotate(img, 1)
        for i, surface in enumerate(credit_surfaces):
            screen.blit(surface, (screen.get_width() // 2 - surface.get_width() // 2, credit_y + i * 40))
        credit_y -= credit_speed
        if credit_y + len(credit_surfaces) * 40 < 0:
            credit_y = screen.get_height()
        pygame.display.flip()
        clock.tick(fps)
    pygame.mixer.music.stop()
