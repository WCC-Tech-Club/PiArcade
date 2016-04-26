import pi_globals

class AnimationController:

	__target = None             # The target sprite (pygame sprite object) that is to be animated

	__spritesheet = None        # Array of surfaces (traditional sprites) to act as animation frames
	__spriteIndex = 0           # Current sprite from the sprite sheet applied to the target

	__animTime = 0.0            # Frame time of current animation strip. Controlled by framerate.
	__animStart = 0             # The start index from the sprite sheet for the animation strip
	__animLength = 1            # The length of the strip to animate

	animFramerate = 30.0        # The number of frames (sprites from the sprite sheet) to cycle through per second
	enabled = False             # boolean flag to control if the controller should animate

	__frameTriggers = dict()	# Functions to tall when passing a specific sprite index frame

	def __init__(self, target, spriteSheet, animFramerate = 30.0):
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

	def setTrigger(self, spriteIndex, trigger):
		self.__frameTriggers[spriteIndex] = trigger;

	def removeTrigger(self, spriteIndex):
		del self.__frameTriggers[spriteIndex]

	def setAnimStrip(self, animStart, animLength, animFrameRate = 30.0):
		self.__animStart = animStart
		self.__animLength = animLength
		self.__animTime = 0.0
		self.animFramerate = animFrameRate

	def update(self):
		if self.enabled:

			lastFrameTime = int(self.__animTime)
			self.__animTime += self.animFramerate * pi_globals.deltaTime
			currentFrameTime = int(self.__animTime)

			if currentFrameTime != lastFrameTime:

				spriteIndex = 0
				frameTriggers = []

				for i in range(lastFrameTime + 1, currentFrameTime + 1):

					frameStep = i % self.animLength

					# If the animation time is negative, this makes the index valid to use
					if frameStep < 0:
						frameStep += self.animLength

					spriteIndex = self.animStart + frameStep

					if spriteIndex in self.__frameTriggers:
						frameTriggers.append(self.__frameTriggers[spriteIndex])

				self.spriteIndex = spriteIndex

				for trigger in frameTriggers:
					trigger(self.__target)
