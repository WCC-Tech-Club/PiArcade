import pi_globals

from pygame.math import *
from pygame.sprite import *

from animation import AnimationController

class Projectile(Sprite):

	__animController = None     # Animation controller for animation

	position = Vector2(0, 0)    # Position in 2D space of the projectile
	velocity = Vector2(0, 0)    # Velocity vector of the projectile
	arcGravity = 0.0            # "Gravity" force of the projectile to simulate an throw arc

	def __init__(self, spriteSheet, collisionRadius, position, velocity, arcGravity = 0):
		Sprite.__init__(self)
		self.image = spriteSheet[0]
		self.rect = self.image.get_rect()
		self.rect.radius = collisionRadius
		self.position = position
		self.velocity = velocity
		self.arcGravity = arcGravity
		self.__animController = AnimationController(self, spriteSheet)

	def getAnimController(self):
		return self.__animController

	animController = property(getAnimController)

	def getCollisionRadius(self):
		return self.rect.radius

	collisionRadius = property(getCollisionRadius)

	# Args[0] is must be delta time (amount in seconds between frames)
	def update(self):

		# add velocity to position taking into account the delta time
		self.position += self.velocity * pi_globals.deltaTime

		# (0, 0) is at the top left corner so arc gravity induces a positive y shift (delta time applied as well)
		self.position.y += self.arcGravity * pi_globals.deltaTime
		if self.position.y > self.arcGravity:
			self.position.y = self.arcGravity

		# Animation
		self.animController.update()

		# Update rect center with position
		self.rect.center = self.position