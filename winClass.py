import pygame, sys, time
from pygame.locals import *

class Win(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY):
        super().__init__()
        self.width = width
        self.height = height
        self.x = posX
        self.y = posY
        self.type = "WIN"
        self.rect = pygame.Rect(self.x, self.y, width, height)
