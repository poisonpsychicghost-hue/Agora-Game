import pygame
pygame.init()
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Agora Practice Window")

n = 0
scripts = ["Press Z...", "Hello Player!", "Welcome to the Game!", "Thank You! \nHave A Wonderful Day!", "GoodBye!"]
script_len = len(scripts)
current_displayed_message = scripts[0]
text_advance_box = scripts[0]

running = True
big_font = pygame.font.SysFont("Arial", 50)
little_font = pygame.font.SysFont("Arial", 16)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                n += 1
                if n < script_len:
                    current_displayed_message = scripts[n]
                else:
                    running = False

    # background to start|FF uses Blueish/Pokemon off-white/Doom dark
    screen.fill((20, 20, 20))

    #play area
    pygame.draw.rect(screen, (225, 225, 225), (16, 16, 608, 250))
    lines = current_displayed_message.split("\n")

    if n < script_len:
        for i, line in enumerate(lines):
            big_text_surface = big_font.render(line, True, (36, 124, 72))
            screen.blit(big_text_surface, (48, 48 + i * 50))
    #Text box area
    pygame.draw.rect(screen, (76, 76, 76), (32, 270, 572, 74))
    pygame.draw.rect(screen, (33, 33, 33), (40, 278, 560, 58))
    pygame.draw.rect(screen, (76, 76, 76), (42, 280, 556, 54))
    text_surface = little_font.render(text_advance_box, True, (0, 0, 0))
    screen.blit(text_surface, (48, 288))

    pygame.display.flip()

pygame.quit()
