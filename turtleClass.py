
#Creates and transforms images to desired size
TURTLE = pygame.image.load('resources/turtle.png')
LOG = pygame.image.load('resources/log.pngs')
LOG = pygame.transform.scale(LOG, (25,25))
TURTLE = pygame.transform.scale(TURTLE, (25,25))

class WaterObject(pygame.sprite.sprite):

    #Sets up all of the values needed to initialize the sprite: the sprite's y position, and determining if it is going to the left or right
    def __init__(self, posY, leftRight):
        self.leftRight = leftRight
        self.y = posY

        #Sets the sprite on the left or right side of the sceen based on which way it is moving
        if self.leftRight == "LEFT":
            self.x = 400
        else:
            self.x == 0
        self.rect = pygame.Rect(self.x, self.y, (25,25))

    #Moves the sprite one tile
    def move(self):
        if self.leftRight == "LEFT":
            self.x -= 25
        else:
            self.x += 25

    #Kills itself if it needs killing, moves itself if it needs moving.
    #***Might have to move the kill into game loop only
    def update(self):
        if self.leftRight == "LEFT":
            if self.rect.x == 0:
                self.kill()
            else:
                self.move()
        else:
            if self.rect.x == 400:
                self.kill()
            else:
                self.move()

#Things for the game loop
onWaterObj = False
global onWaterObj

#Detects collisions between the frog and any object in the water
#Loops through the sprite group to get which exact log the frog is on
for loop in waterObjects:
    if pygame.sprite.collide_rect(frog, loop):
        onWaterObj = loop
if onWaterObj != False:
    frog.rect.x = onWaterObj.rect.x
