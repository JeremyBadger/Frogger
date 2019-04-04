import pygame, sys, time, random
from pygame.locals import *

CAR= pygame.image.load('resources/car.png')
CAR2= pygame.image.load('resources/car.png')


class cars(pygame.sprite.Sprite):
    def __init__(self, ground):
        super().__init__()
        self.x=400
        self.y=ground
        self.rect=pygame.Rect(self.x,self.y,25,35)
        self.image=CAR
        self.type = "CAR"


    def move(self):
        if self.x>-100:
            self.rect.x -= 10
        elif self.x<= -100:
            self.x=500
