import pygame, sys, time, random #importing librarys
from pygame.locals import *

CAR= pygame.image.load('resources/car.png') #calling the same image for both the car variables
CAR2= pygame.image.load('resources/car.png')


class cars(pygame.sprite.Sprite):
    def __init__(self, ground, leftRight, speed): #the init function setting all the variables
        super().__init__()
        self.x=0
        self.y=ground
        self.leftRight = leftRight
        self.image=CAR
        self.speed = speed
        self.type = "CAR"
        if self.leftRight == "LEFT": #setting up all the cars going to the left/right
            self.x = 400
        else:
            self.x = 0
        self.rect=pygame.Rect(self.x,self.y,10,10) #car hitboxes

    def update(self):    #determining how fast each car moves and when they respawn back on the screen
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
