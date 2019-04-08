import pygame
from pygame.locals import *
FROG = pygame.image.load('resources/frog.png')

class frog(pygame.sprite.Sprite):
    def __init__(self):
        #When frog calss is ran
        super().__init__()
        self.image = FROG
        #Image name
        self.imgage = pygame.transform.scale(FROG, (25,25))
        #Size of image
        self.points = 0
        self.x = 200
        self.y = 280
        #Spawn
        self.rect = pygame.Rect(self.x, self.y, 25, 25)
        #Hitbozx

    def up(self):
        #Up key
        self.rect.y = self.rect.y - 25
        #Moves down
        self.points = self.points + 100
        #Gains 100 points
        if self.rect.y < 0:
            self.kill()
            #Dies off screen

    def left(self):
        self.rect.x = self.rect.x - 25
        #Moves left
        if self.rect.x < 0:
            self.kill()
            #Dies off screen
    def right(self):
        self.rect.x = self.rect.x + 25
        #Moves Right
        if self.rect.x > 400:
            self.kill()
            #Dies off Screen

    def down(self):
        self.rect.y = self.rect.y + 25
        #Moves Down
        self.points = self.points - 100
        #Losses 100 points
        if self.rect.y < 0:
            self.kill()
            #Dies off screen
