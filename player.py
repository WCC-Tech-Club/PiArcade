from pygame.math import *
from pygame.sprite import *

class Player(Sprite):

	position = Vector2(0, 0)
	velocity = Vector2(0, 0)

	def __init__(self):
		Sprite.__init__(self)