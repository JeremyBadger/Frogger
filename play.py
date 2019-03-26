import pygame, sys, time
from pygame.locals import *

from frogClass import frog
from carClass import cars
from turtleClass import WaterObject
from waterClass import Water

frog = frog()
car = cars(250)
turtles = turtle(75, "LEFT")
water = water(400,100,0,25)

enemy = pygame.sprite.Group()

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)

BACKGROUND = ('resources/background.png')

game_over = False

waterObjects = pygame.sprite.Group()

def add_cars():
    if time % 120 == 0:
        enemy.add(car)

def update_cars():
    for car1 in enemy:
        car1.move()
        car1.update()
        DISPLAYSURF.blit(car1.image, car1.rect)

#def update_frog():

def add_turtles():
    if time % 120 == 0:
        enemy.add(turtle)

#def add_logs():
#    if time % 120 == 0:
#        waterObjects.add(log)

def update_turtles():
    for turtle1 in waterObjects:
        turtle1.update()
        DISPLAYSURF.blit(turtle1.image, turtle1.rect)

#def update_logs():
#    for log1 in waterObjects:
#        log1.update()
#        DISPLAYSURF.blit(log1.image, log1.rect)

#def scorebox():

def is_collision():
    global game_over
    if pygame.sprite.spritecollideany(frog, enemy):
        game_over = True
    else:
        game_over = False

def game_over():
    global game_over
    if game_over == True:
        display_message("Game over.")

DISPLAYSURF.blit(frog.image,frog.rect)
while True:
    if game_over == True:
        frog.kill()
        cars.kill()
        turtle.kill()
        log.kill()
        game_over()
    if game_over == False:
        add_cars()
        update_cars()
        add_turtles()
        add_logs()
        update_turtles()
        update_logs()
        scorebox()
    if event.type==KEYDOWN:
        if event.key==K_UP:
            frog.up(25)
        if event.key==K_DOWN:
            frog.down(25)
        if event.key==K_LEFT:
            frog.left(25)
        if event.key==K_RIGHT:
            frog.right(25)
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
