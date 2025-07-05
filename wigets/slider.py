import pygame

class Slider():
    def __init__(self, screen, x= 15, y= 15, width = 200, height=35, color=(0,0,0), max_value=1, value=0.5):
        self.value = value
        self.max_value = max_value
        
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width*(self.value/self.max_value), self.height), border_radius=5)
        pygame.draw.rect(self.screen, (50,50,50), (self.x, self.y, self.width, self.height), width=2, border_radius=5)
