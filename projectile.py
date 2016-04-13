from pygame.math import *
from pygame.sprite import *

class Projectile(Sprite):

	__renderImages = None       # Array of images used to render the projectile
	__renderIndex = 0           # Current index used to select a image

	animate = False             # Flat to determine if the projectile should animate
	animFrameRate = 0.0         # Number of render images cycled per second
	__animTime = 0.0            # Global animation time, constant used to calculate correct render index
	__animStart = 0             # The starting render index to use (inclusive)
	__animLength = 0            # The number if render images that make up the animation

	position = Vector2(0, 0)    # Position in 2D space of the projectile
	velocity = Vector2(0, 0)    # Velocity vector of the projectile
	arcGravity = 0.0            # "Gravity" force of the projectile to simulate an throw arc

	collisionRadius = 0.0       # Circle collider radius centered at position

	def __init__(self, renderImages, collisionRadius, position, velocity, arcGravity = 0):
		Sprite.__init__(self)
		self.image = None
		self.rect = None

		self.collisionRadius = collisionRadius
		self.position = position
		self.velocity = velocity
		self.arcGravity = arcGravity

		self.__renderImages = renderImages
		self.setRenderIndex(0)

	def getRenderIndex(self):
		return self.__renderIndex

	def setRenderIndex(self, renderIndex):
		if renderIndex == self.__renderIndex:
			pass

		self.__renderIndex = renderIndex
		self.image = self.__renderImages[renderIndex]

		# Something tells me this is bad to do seeing as it will be called quite often (this creates a new rect object I think)
		self.rect = self.image.get_rect(center = self.position, radius = self.collisionRadius)

	renderIndex = property(getRenderIndex, setRenderIndex)

	def getAnimStart(self):
		return self.__animStart

	animStart = property(getAnimStart)

	def getAnimLength(self):
		return self.__animLength

	animLength = property(getAnimLength)

	def setAnimStrip(self, animStart, animLength):
		self.__animStart = animStart
		self.__animLength = animLength
		self.__animTime = 0.0
		self.setRenderIndex(animStart)

	# Args[0] is must be delta time (amount in seconds between frames)
	def update(self, *args):

		# add velocity to position taking into account the delta time
		self.position += self.velocity * args[0]

		# (0, 0) is at the top left corner so arc gravity induces a positive y shift (delta time applied as well)
		self.position.y += self.arcGravity * args[0]
		if self.position.y > self.arcGravity:
			self.position.y = self.arcGravity

		# Animation
		if self.animate:
			self.__animTime += self.animFrameRate * args[0]
			animStep = int(self.__animTime) % self.animLength

			# If the animation time is negative, this makes the index valid to use
			if animStep < 0:
				animStep += self.animLength

			self.setRenderIndex(animStep + self.animStart)

		self.rect.center = self.position