class Water(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY):
        super().__init__()
        self.x = posX
        self.y = posY
        self.image = pygame.image.load('PLACEHOLDER')
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = pygame.Rect(self.x, self.y, width, height)
