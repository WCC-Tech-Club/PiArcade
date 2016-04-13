from pygame.math import *
from pygame.sprite import *

class Projectile(Sprite):

	position = Vector2(0, 0)
	velocity = Vector2(0, 0)

	def __init__(self, position, velocity):
		Sprite.__init__(self)
		self.position = position
		self.velocity = velocity

	# Args[0] is must be delta time (amount in seconds between frames)
	def update(self, *args):
		self.position += self.velocity * args[0]

		# Apply projectile gravity if necessary
		# Apply position values to rect for use in rendering