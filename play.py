import pygame, sys, time
from pygame.locals import *

from frogClass import frog
from carClass import cars
from turtleClass import turtle
from waterClass import water

pygame.init()


frogger = frog(150)
car = cars(150)
turtles = turtle(150)
log = water(150)

enemy = pygame.sprite.Group()

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)

BACKGROUND = ('resources/background.png')

game_over = False

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

def add_logs():
    if time % 120 == 0:
        enemy.add(log)

def update_turtles():
    for turtle1 in enemy:
        turtle1.move()
        turtle1.update()
        DISPLAYSURF.blit(turtle1.image, turtle1.rect)

def update_logs():
    for log1 in enemy:
        log1.move()
        log1.update()
        DISPLAYSURF.blit(log1.image, log1.rect)

#def scorebox():

def is_collision():
    global game_over
    if pygame.sprite,spritecollideany(frog, enemy):
        game_over = True
    else:
        game_over = False

def game_over():
    global game_over
    if game_over == True:
        display_message("Game over.")

DISPLAYSURF.blit(rex.image,rex.rect)
while True:
    if game_over == True:
        frog.kill()
        cars.kill()
        turtle.kill()
        log.kill()
        game_over()
    if game_over == False:
        DISPLAYSURF.blit(frogger.image, frogger.rect)
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
