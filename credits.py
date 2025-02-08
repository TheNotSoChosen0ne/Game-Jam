import pygame

def credits(screen, clock, fps=30):
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Set up the font
    font = pygame.font.Font("pixel_font.otf", 42)

    # Credits text
    credits = [
        "Script: Loann Badina",
        "Art: Nicolas Bach",
        "Game Developer: Lilian Locher",
        "Game Developer: Thibaut Musslin",
        "",
        "Yanis With: Bonsoir jeune aventurier, veux-tu faire la quête du forgeron ?",
        "",
        "Special Thanks: Mr. Guillaumat",
        "Special Thanks: Fab",
        "Special Thanks: Lorem Ipsum",
    ]

    # Create a list of rendered text surfaces
    credit_surfaces = [font.render(line, True, WHITE) for line in credits]

    # Initial position of the credits
    credit_y = screen.get_height()

    # Speed of the credits
    credit_speed = 3

    # Main loop for credits
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Clear the screen
        screen.fill(BLACK)

        # Draw the credits
        for i, surface in enumerate(credit_surfaces):
            screen.blit(surface, (screen.get_width() // 2 - surface.get_width() // 2, credit_y + i * 40))

        # Update the position of the credits
        credit_y -= credit_speed

        # If the credits have moved off the top of the screen, reset their position
        if credit_y + len(credit_surfaces) * 40 < 0:
            credit_y = screen.get_height()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(fps)
