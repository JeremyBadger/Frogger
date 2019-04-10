import pygame, sys, time
from pygame.locals import *

from frogClass import frog
from carClass import cars
from turtleClass import *
from waterClass import Water

frog = frog()
car = cars(225)
water = Water(400,70,0,25)

FPS = 10
time = 0

pygame.init()

fpsClock = pygame.time.Clock()

waterObjects = pygame.sprite.Group()
enemy = pygame.sprite.Group()
#cars = pygame.sprite.Group()
enemy.add(water)

DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption("Frogger")

BACKGROUND = pygame.image.load('resources/background.png')
background_x = 0
background_y = 0

global onWaterObj
onWaterObj = False

game_over = False

text = ""
def add_cars():
    if time % 120 == 0:
        car = cars(225)
        enemy.add(car)

def update_cars():
    for car1 in enemy:
        if car1.type == "CAR":
            car1.move()
            car1.update()
            DISPLAYSURF.blit(car1.image, car1.rect)
    if car.rect.x < 0 or car.rect.x > 400:
        car.kill()
    elif car.rect.y < 0 or car.rect.y > 300:
        car.kill()

#def update_frog():

def add_turtles():
    if time % 30 == 0:
        turtles = WaterObject(100, "LEFT", 6)
        turtles2 = WaterObject(75, "RIGHT", 5)
        waterObjects.add(turtles)
        waterObjects.add(turtles2)
    if time % 20 == 0:
        turtles3 = WaterObject(50, "RIGHT", 7)
        waterObjects.add(turtles3)
    if time % 40 == 0:
        turtles4 = WaterObject(25, "LEFT", 8)
        waterObjects.add(turtles4)

def add_logs():
    if time % 120 == 0:
        waterObjects.add(log)

def update_turtles():
    for turtle1 in waterObjects:
        turtle1.update()
        DISPLAYSURF.blit(turtle1.image, turtle1.rect)

#def update_logs():
#    for log1 in waterObjects:
#        log1.update()
#        DISPLAYSURF.blit(log1.image, log1.rect)

def scorebox(text):
    BASICFONT = pygame.font.Font("freesansbold.ttf", 16)
    Surf = BASICFONT.render(text, 1, (0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = (10, 10)
    DISPLAYSURF.blit(Surf, Rect)

def is_collision():
    global game_over
    if pygame.sprite.spritecollideany(frog, enemy) and not pygame.sprite.spritecollideany(frog, waterObjects):
        game_over = True
        return game_over
    else:
        game_over = False
        return game_over
def game_over():
    global game_over
    if game_over == True:
        scorebox("Game over.")

while True:
    DISPLAYSURF.blit(BACKGROUND,(background_x, background_y))
    update_turtles()
    DISPLAYSURF.blit(frog.image,(frog.rect.x, frog.rect.y))
    if game_over == True:
        pygame.quit()
        sys.exit()
        #frog.kill()
        #car.kill()
        #turtle.kill()
        #log.kill()
        #game_over()
    if game_over == False:
        add_cars()
        update_cars()
        add_turtles()
        #add_logs
        #update_logs()
        scorebox("Score: " + str(frog.points))
        time += 1
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    frog.up()
                    onWaterObj = False
                if event.key==K_DOWN:
                    frog.down()
                    onWaterObj = False
                if event.key==K_LEFT:
                    frog.left()
                if event.key==K_RIGHT:
                    frog.right()

    #Detects collisions between the frog and any object in the water
    #Loops through the sprite group to get which exact log the frog is on
    for loop in waterObjects:
        if pygame.sprite.collide_rect(frog, loop):
            onWaterObj = loop
    if onWaterObj != False:
        frog.rect.x = onWaterObj.rect.x
    game_over = is_collision()
    pygame.display.update()
    fpsClock.tick(FPS)
