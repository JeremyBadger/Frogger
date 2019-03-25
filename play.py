import pygame, sys, time
from pygame.locals import *

from frogClass import frog
from carClass import cars
from turtleClass import turtle
from waterClass import water

pygame.init()

game_over = False

def add_cars():

def update_cars():

def update_frog():

def add_turtles():

def add_logs():

def update_turtles():

def update_logs():

def scorebox():

def is_collision():
    global game_over
    if pygame.sprite,spritecollideany(frog, enemy):
        game_over = True
    else:
        game_over = False

DISPLAYSURF.blit(rex.image,rex.rect)
while True:
    if game_over == True:
        frog.kill()
        cars.kill()
        turtle.kill()
        log.kill()
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
            x.up(25)
        if event.key==K_DOWN:
            x.down(25)
        if event.key==K_LEFT:
            x.left(25)
        if event.key==K_RIGHT:
            x.right(25)
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
