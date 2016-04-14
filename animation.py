from pygame.sprite import *

class AnimationController:

	__target = None

	__spritesheet = None
	__spriteIndex = 0

	__animTime = 0.0
	__animStart = 0
	__animLength = 1

	animFramerate = 30.0
	enabled = True

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

	def update(self, deltaTime):
		if self.enabled:
			self.__animTime += self.animFramerate * deltaTime
			animStep = int(self.__animTime) % self.animLength

			# If the animation time is negative, this makes the index valid to use
			if animStep < 0:
				animStep += self.animLength

			self.spriteIndex = animStep + self.animStart
