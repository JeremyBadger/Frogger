TURTLE = pygame.image.load('resources/turtle.png')
LOG = pygame.image.load('resources/log.pngs')
LOG = pygame.transform.scale(LOG, (25,25))
TURTLE = pygame.transform.scale(TURTLE, (25,25))
class WaterObject(pygame.sprite.sprite):
    def __init__(self, posY, leftRight):
        self.leftRight = leftRight
        self.y = posY
        if self.leftRight == "LEFT":
            self.x = 400
        else:
            self.x == 0
        self.rect = pygame.Rect(self.x, self.y, (25,25))
    def move(self, self.leftRight):
        if self.leftRight == "LEFT":
            self.x -= 25
        else:
            self.x += 25

#if pygame.sprite.spritecollideany(frog, waterObjects):
#    frog.rect.x = 
