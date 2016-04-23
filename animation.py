import pi_globals

from pygame.sprite import Sprite

class AnimationController:

	__target = None             # The target sprite (pygame sprite object) that is to be animated

	__spritesheet = None        # Array of surfaces (traditional sprites) to act as animation frames
	__spriteIndex = 0           # Current sprite from the sprite sheet applied to the target

	__animTime = 0.0            # Time in seconds an animation strip has been playing
	__animStart = 0             # The start index from the sprite sheet for the animation strip
	__animLength = 1            # The length of the strip to animate

	animFramerate = 30.0        # The number of frames (sprites from the sprite sheet) to cycle through per second
	enabled = False             # boolean flag to control if the controller should animate

	def __index__(self, target, spriteSheet, animFramerate = 30.0):
		self.__target = target
		self.__spritesheet = spriteSheet
		self.setAnimStrip(0, len(spriteSheet), animFramerate)

	def getSpriteIndex(self):
		return self.__spriteIndex

	def setSpriteIndex(self, spriteIndex):
		self.__spriteIndex = spriteIndex
		self.__target.image = self.__spritesheet[spriteIndex]

	spriteIndex = property(getSpriteIndex, setSpriteIndex)

	def getAnimStart(self):
		return self.__animStart

	animStart = property(getAnimStart)

	def getAnimLength(self):
		return self.__animLength

	animLength = property(getAnimLength)

	def setAnimStrip(self, animStart, animLength, animFrameRate = 30.0):
		self.__animStart = animStart
		self.__animLength = animLength
		self.__animTime = 0.0
		self.animFramerate = animFrameRate
		self.spriteIndex = animStart

	def update(self):
		if self.enabled:
			self.__animTime += self.animFramerate * pi_globals.deltaTime
			animStep = int(self.__animTime) % self.animLength

			# If the animation time is negative, this makes the index valid to use
			if animStep < 0:
				animStep += self.animLength

			self.spriteIndex = animStep + self.animStart
