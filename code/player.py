from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((48,56))
        self.image.fill('red')
        self.rect = self.image.get_frect(topleft = pos)

        # movement
        self.direction = vector(1, 0)
        self.speed = 0.1

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            print('right')

    def move(self):
        self.rect.topleft += self.direction * self.speed

    def update(self):
        self.input()
        self.move()