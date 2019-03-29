import pygame, sys, time
from pygame.locals import *

from frogClass import frog
from carClass import cars
waterObjects = pygame.sprite.Group()
from turtleClass import *
from waterClass import Water

frog = frog()
car = cars(250)
turtles = WaterObject(75, "LEFT")
water = Water(400,100,0,25)

FPS = 10

fpsClock = pygame.time.Clock()

enemy = pygame.sprite.Group()
enemy.add(water)

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption("Frogger")

BACKGROUND = pygame.image.load('resources/background.png')
background_x = 0
background_y = 0

game_over = False


def add_cars():
    if time % 120 == 0:
        enemy.add(car)

def update_cars():
    for car1 in enemy:
        car1.move()
        car1.update()
        DISPLAYSURF.blit(car1.image, car1.rect)
    if car.rect.x <= 0 or car.rect.x >= 400:
        car1.kill()
    elif car.rect.y <= 0 or car.rect.y >= 300:
        car1.kill()

#def update_frog():

def add_turtles():
    if time % 120 == 0:
        waterObjects.add(turtle)

#def add_logs():
#    if time % 120 == 0:
#        waterObjects.add(log)

def update_turtles():
    for turtle1 in waterObjects:
        turtle1.update()
        DISPLAYSURF.blit(turtle1.image, turtle1.rect)
    if turtle.rect.x <= 0 or turtle.rect.x >= 400:
        turtle1.kill()
    elif turtle.rect.y <= 0 or turtle.rect.y >= 300:
        turtle1.kill()

#def update_logs():
#    for log1 in waterObjects:
#        log1.update()
#        DISPLAYSURF.blit(log1.image, log1.rect)

def scorebox():
    BASICFONT = pygame.font.Font("freesansbold.ttf", 16)
    Surf = BASICFONT.render(text, 1, (0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = (10, 10)
    DISPLAYSURF.blit(Surf, Rect)
    display_message("Score: " + str(frogger.score))

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

while True:
    DISPLAYSURF.blit(BACKGROUND,(background_x, background_y))
    DISPLAYSURF.blit(frog.image,frog.rect)
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
        #add_logs()
        update_turtles()
        #update_logs()
        scorebox()

    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    frog.up()
                if event.key==K_DOWN:
                    frog.down()
                if event.key==K_LEFT:
                    frog.left()
                if event.key==K_RIGHT:
                    frog.right()
    add_turtles()
    pygame.display.update()
    fpsClock.tick(FPS)
