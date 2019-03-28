import pygame
from pygame.locals import *
FROG = pygame.image.load('resources/frog.png')

class frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = FROG
        self.imgage = pygame.transform.scale(FROG, (25,25))
        self.rect = pygame.Rect(25,25,25,25)
        self.points = 0
        self.x = 275
        self.y = 200

    def up(self):
        self.rect.y = self.rect.y - 20
        self.points = self.points + 100
        if self.rect.y < 0:
            self.kill()

    def left(self):
        self.rect.x = self.rect.x - 25
        if self.rect.x < 0:
            self.kill()

    def right(self):
        self.rect.x = self.rect.x + 25
        if self.rect.x > 400:
            self.kill()

    def down(self):
        self.rect.y = self.rect.y + 25
        self.points = self.points - 100
        if self.rect.y < 0:
            self.kill()
