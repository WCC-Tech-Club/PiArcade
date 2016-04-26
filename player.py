from pygame.math import *
from pygame.sprite import *

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
		self.__animController = AnimationController(self, spriteSheet)

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
        #Change center to tiop half
		bullet_origin = self.rect.center


