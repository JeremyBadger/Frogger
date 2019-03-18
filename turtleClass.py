TURTLE = pygame.image.load('resources/turtle.png')
LOG = pygame.image.load('resources/log.pngs')
class WaterObject(pygame.sprite.sprite):
    def __init__(self, posY, leftRight):
        #things
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
