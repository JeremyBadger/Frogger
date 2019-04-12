import pygame, sys, time, random
from pygame.locals import *

CAR= pygame.image.load('resources/car.png')
CAR2= pygame.image.load('resources/car.png')


class cars(pygame.sprite.Sprite):
    def __init__(self, ground, leftRight, speed):
        super().__init__()
        self.x=0
        self.y=ground
        self.leftRight = leftRight
        self.image=CAR
        self.speed = speed
        self.type = "CAR"
        if self.leftRight == "LEFT":
            self.x = 400
        else:
            self.x = 0
        self.rect=pygame.Rect(self.x,self.y,10,10)

    def update(self):
        if self.leftRight == "LEFT":
            if self.x>0:
                self.rect.x -= self.speed
            elif self.x < 0:
                self.kill()
        else:
            if self.x < 400:
                self.rect.x += self.speed
            else:
                self.kill()
