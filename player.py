import pygame
import input as inp
import colors as color
import debug
import math
debuger = debug.Debuger()
#debuger.start_log()
debuger.tweak_setup(0.1, 7.0)

class Player():    
    def __init__(self, screen):
        self.x = 100
        self.y = 100
        self.x_speed = 0
        self.y_speed = 0
        self.screen = screen
        self.accleration = 1.0
        self.friction = 0.54
        self.accleration_scaled = self.accleration

    def update(self):
        self.update_pos()
        self.update_speed()
        debuger.log("y_speed: ", self.y_speed)
        debuger.log("y", self.y)
        self.accleration = debuger.tweak()    

    def update_pos(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.x_speed *= self.friction
        self.y_speed *= self.friction
        pygame.draw.rect(self.screen, color.black, (self.x, self.y, 50, 50))

    def update_speed(self):
        if (inp.get_keys("w") or inp.get_keys("s")) and (inp.get_keys("a") or inp.get_keys("d")):
            self.accleration_scaled = math.sqrt((self.accleration*self.accleration)/2)
        else:
            self.accleration_scaled = self.accleration


        if inp.get_keys("w"):
            self.y_speed -= self.accleration_scaled

        if inp.get_keys("s"):
            self.y_speed += self.accleration_scaled

        if inp.get_keys("a"):
            self.x_speed -= self.accleration_scaled

        if inp.get_keys("d"):
            self.x_speed += self.accleration_scaled