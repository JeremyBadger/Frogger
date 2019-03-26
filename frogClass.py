import pygame
from pygame.locals import *


class frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = 'frog.png'
        self.imgage = pygame.transform.scale('frog.png', (25,25))
        self.rect = pygame.Rect(25,25,25,25)
        points = 0
        self.x = 275
        self.y = 200
        frog = frogClass(self.x,self.y)

    def up(self):
        self.rect.y = self.rect.y - 20
        points = points + 100

    def left(self):
        self.rect.x = self.rect.x - 25

    def right(self):
        self.rect.x = self.rect.x + 25

    def down(self):
        self.rect.y = self.rect.y + 25
        points = points - 100
