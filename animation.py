import pi_globals

class Animation:

	__sprites = []              # Sprites that make up the animation
	__framerate = 30.0          # Framerate (number of sprites to cycle through per second)
	__frameEvents = dict()           # events to fire when specific frames are passed

	def __init__(self, sprites, framerate = 30.0):
		self.__sprites = sprites
		self.framerate = framerate

	def __getFrameCount(self):
		return len(self.__sprites)

	def getSprite(self, frame):
		return self.__sprites[frame];

	def __getFramerate(self):
		return self.__framerate

	def __setFramerate(self, framerate):
		if framerate < 0:
			framerate = 0

		self.__framerate = framerate

	def setFrameEvent(self, frame, event):
		self.__frameEvents[frame] = event

	def hasEventAtFrame(self, frame):
		return frame in self.__frameEvents

	def getEventAtFrame(self, frame):
		return self.__frameEvents[frame]

	def removeFrameEvent(self, frame):
		del self.__frameEvents[frame]

	frameCount = property(__getFrameCount)

	framerate = property(__getFramerate, __setFramerate)


class AnimationController:

	__target = None                 # The target sprite (pygame sprite object) that is to be animated
	__animations = []               # A list of animations this controller manages
	__playingAnimationIndex = 0     # The current animation playing

	__animTime = 0.0                # Frame time of current animation strip. Controlled by framerate.

	__isEnabled = False             # boolean flag to control if the controller should animate

	def __init__(self, target, animations, startAnimation = 0):
		self.__target = target
		self.__animations = animations
		self.playingAnimationIndex = startAnimation

	def __hasTarget(self):
		return self.__target is not None

	def __getTarget(self):
		return self.__target

	def __getAnimationCount(self):
		return len(self.__animations)

	def getAnimation(self, index):
		return self.__animations[index]

	def __getPlayingAnimationIndex(self):
		return self.__playingAnimationIndex

	def __setPlayingAnimationIndex(self, index):
		if index == self.__playingAnimationIndex:
			pass

		self.__playingAnimationIndex = index
		self.__target.image = self.playingAnimation.getSprite(0)
		self.__animTime = 0.0

	def __getPlayingAnimation(self):
		return self.getAnimation(self.__playingAnimationIndex)

	def __getIsEnabled(self):
		return self.__isEnabled

	def __setIsEnabled(self, isEnabled):
		self.__isEnabled = isEnabled

	hasTarget = property(__hasTarget)

	target = property(__getTarget)

	animationCount = property(__getAnimationCount)

	playingAnimationIndex = property(__getPlayingAnimationIndex, __setPlayingAnimationIndex)

	playingAnimation = property(__getPlayingAnimation)

	isEnabled = property(__getIsEnabled, __setIsEnabled)

	def update(self):

		if self.isEnabled and self.hasTarget and self.playingAnimation.framerate > 0.0:

			lastFrameTime = int(self.__animTime)
			self.__animTime += self.playingAnimation.framerate * pi_globals.deltaTime
			currentFrameTime = int(self.__animTime)

			if currentFrameTime > lastFrameTime:

				frame = 0
				frameEvents = []

				for frameTime in range(lastFrameTime + 1, currentFrameTime + 1):

					frame = frameTime % self.playingAnimation.frameCount

					# If the animation time is negative, this makes the index valid to use
					if frame < 0:
						frame += self.playingAnimation.frameCount

					if self.playingAnimation.hasEventAtFrame(frame):
						frameEvents.append(self.playingAnimation.getEventAtFrame(frame))

				self.target.image = self.playingAnimation.getSprite(frame)

				for frameEvent in frameEvents:
					frameEvent(self.__target)

