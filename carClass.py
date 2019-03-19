import pygame, sys, time, random
from pygame.locals import *

CAR= pygame.image.load('resources/car.png')

class cars(pygame.sprite.Sprite):
    def __init__(self, ground):
        super().__init__()
        self.x=156
        self.y=280
        self.rect=pygame.Rect(self.x,self.y,25,35)
        self.image=CAR

    def move(self):
        if self.x>-100:
            self.x=self.x-3
            self.rect.x=self.x
            self.rect.y=100
        elif self.x<= -100:
            self.x=500
