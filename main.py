import pygame
import player as pl


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hallo Welt")
clock = pygame.time.Clock()

player_main = pl.Player(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    
    player_main.update()

    clock.tick(60)
    pygame.display.flip()