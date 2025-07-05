import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hallo Welt")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    pygame.draw.rect(screen, (0,0,0), (50,50,50,50))

    pygame.display.flip()