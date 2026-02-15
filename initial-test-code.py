import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Agora Test Window")
screen.fill((165, 180, 165))  # Fill background
pygame.draw.rect(screen, (120, 170, 230), (0, 0, 600, 400))  # rectangle replaces fill at these values
pygame.display.flip()

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()