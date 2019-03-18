import pygame, sys, time, random
from pygame.locals import *

CAR= pygame.image.load('resources/car.png')

class cars(pygame.sprite.Sprite):
    def __init__(self, ground):
        super().__init__()
        self.x=25
        self.y=25
        self.rect=pygame.Rect(self.x,self.y,25,35)
        self.image=CAR

    def move(self):
