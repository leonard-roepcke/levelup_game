import pygame
import player as pl
from wigets import slider
import colors
import debug

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hallo Welt")
clock = pygame.time.Clock()

debuger = debug.Debuger()
debuger.tweak_setup(0, 1)

player_main = pl.Player(screen)
live_slider = slider.Slider(screen, color=colors.green)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    
    player_main.update()
    live_slider.draw()
    live_slider.value = debuger.tweak()

    clock.tick(60)
    pygame.display.flip()