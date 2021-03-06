from pygame.math import *
from pygame.sprite import *

from animation import Animation
from animation import AnimationController


class Player(Sprite):

    __animController = None

    position = Vector2(0, 0)

    def __init__(self, spriteSheet, collisionRadius, position):
        Sprite.__init__(self)
        self.image = spriteSheet[0]
        self.rect = self.image.get_rect()
        self.radius = collisionRadius
        self.position = position
        self.__animController = AnimationController(self, [Animation([spriteSheet[0]], 0.0), Animation([spriteSheet[1], spriteSheet[2], spriteSheet[3], spriteSheet[4], spriteSheet[5], spriteSheet[6]], 18.0)])

    def getAnimController(self):
        return self.__animController

    animController = property(getAnimController)

    def getCollisionRadius(self):
        return self.rect.radius

    collisionRadius = property(getCollisionRadius)

    # Args[0] is must be delta time (amount in seconds between frames)
    def update(self):
        # Animation
        self.animController.update()

        # Update rect center with position
        self.rect.center = self.position

    def Shoot(self):
        # Change center to top half
        # bullet_origin = self.rect.center + 5
        pass
