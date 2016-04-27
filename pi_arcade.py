import math

import pygame.key
import pygame.draw
import pygame.sprite

import pi_globals

import arcadeUtils as util

from pygame import display
from pygame.time import Clock
from pygame.math import Vector2
from pygame.sprite import Group
from pygame.sprite import GroupSingle

from projectile import Projectile
from spritesheet import SpriteSheet
from player import Player

# Initialize pygame
pygame.init()

# Set the display mode to full screen with monitor resolution
screenSurface = pygame.display.set_mode((800, 600))
# screenSurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pi_globals.screenSize = screenSurface.get_size()

# Game loop clock
clock = Clock()

# Game loop will run until this is false
running = True

# Sprites & Sprite Groups
<<<<<<< HEAD
player = Player(SpriteSheet("resources/img/player.png").images_at(util.gen_sprite_list(7, 7, 128, 192, 0), [255, 0, 255]), 64,Vector2(128, pi_globals.screenSize[1] / 2.0))
player.animController.enabled = True
#projectile = Projectile(SpriteSheet("resources/img/paper_animation.png").image_at(util.gen_sprite_list(26, 10, 50, 50, 0), [255, 255, 255]), 25, player.position, Vector2(25, 25), 0.0)


def endTrowTrigger(targetPlayer):
    targetPlayer.animController.setAnimStrip(0, 1, 18.0)

=======
player = Player(SpriteSheet("resources/img/player.png").images_at(util.gen_sprite_list(7, 7, 128, 192, 0), [255, 0, 255]), 64, Vector2(128, pi_globals.screenSize[1] / 2.0))
player.animController.isEnabled = True

def endThrowFrameEvent(targetPlayer):
	targetPlayer.animController.playingAnimationIndex = 0
>>>>>>> origin/master

player.animController.getAnimation(1).setFrameEvent(5, endThrowFrameEvent)

playerGroup = GroupSingle(player)
projectileGroup = Group(projectile)

# Joystick initialization
# TODO Move joystick stuff to a input management file
pygame.joystick.init()
hasJoystick = False
joystick = None

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    hasJoystick = joystick.get_numaxes() >= 2

print("Has Joystick: " + str(hasJoystick))

# -------- Main Program Loop -----------
while running:

<<<<<<< HEAD
    # TODO Move input event stuff to input management file
    # Do we even need to use this? All input will be coming from joystick stuff
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                player.animController.setAnimStrip(1, 6, 18.0)
        projectile = Projectile()
        # I dont think we need x position, player only moves along y axis
        projectile.rect.x = player.rect.x
        projectile.rect.y = player.rect.y
=======
	# TODO Move input event stuff to input management file
	# Do we even need to use this? All input will be coming from joystick stuff
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			if event.key == pygame.K_SPACE:
				player.animController.playingAnimationIndex = 1
>>>>>>> origin/master

    screenSurface.fill(pi_globals.BLACK)

    position = Vector2(0, 0)
    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[pygame.K_w] or pressedKeys[pygame.K_UP]:
        position.y -= 1

    if pressedKeys[pygame.K_s] or pressedKeys[pygame.K_DOWN]:
        position.y += 1

    # Hard Coded Speed
    player.position += position * 10;

    playerGroup.update()

    playerGroup.draw(screenSurface)

    # Update screen with what has been drawn
    display.flip()

    # Game loop clock tick and delta time calculation
    pi_globals.deltaTime = clock.tick_busy_loop(pi_globals.FRAMERATE) / 1000.0

# Close the window and quit.
pygame.quit()

######## Refrence Player ########

# Player class with hard coded sprite
# class Player(pygame.sprite.Sprite):
#
# 	def __init__(self, center, anim_framerate=60.0):
# 		pygame.sprite.Sprite.__init__(self)
# 		self.currentSpriteLocation = "resources/img/" + "flying_enemies.png"
# 		# Hard coded sprite loading
# 		self.spriteSheet = spritesheet.SpriteSheet(self.currentSpriteLocation)
# 		self.spriteCount = 0
#
# 		self.sprites = []
# 		self.animFramerate = anim_framerate
# 		self.animTime = 0
#
# 		self.reload_sprites(util.gen_sprite_list(11,11,128,64,0),11,[255,0,255])
# 		print(util.gen_sprite_list(10,10,192,64,1))
# 		self.image = None
# 		self.rect = None
# 		self.set_image(0, center)
#
# 	def get_anim_framerate(self):
# 		return self.animFramerate
#
# 	def set_anim_framerate(self, anim_framerate):
# 		self.animFramerate = anim_framerate
#
# 	def reload_sprites(self,currSpriteSheet,numSprites,ColorKey):
# 		#currSpriteSheet: Array of sprite sheet tuple values (Created by gen_sprite_list)
# 		#numSprites: Number of total sprites
# 		#ColorKey: Color key for spriteSheet.images_at arg
#
# 		# Iterates Sprite loacation list from left to right, top to bottom
# 		self.sprites = self.spriteSheet.images_at(currSpriteSheet,ColorKey)
# 		self.spriteCount = numSprites
# 	def set_image(self, sprite_index, center):
# 		self.image = self.sprites[sprite_index]
# 		self.rect = self.image.get_rect()
# 		self.rect.center = center
#
# 	def update(self, *args):
# 		self.animTime += self.animFramerate * args[0]
# 		image_index = int(self.animTime) % self.spriteCount
#
# 		# If the animation time is negative, this makes the index valid to use
# 		if image_index < 0:
# 			image_index += self.spriteCount
#
# 		self.set_image(image_index, args[1])

######## Refrence Main Loop ########

# position = [size[0] / 2, size[1] / 2]
# player = pygame.sprite.GroupSingle(Player(position, 30.0))
# circleRadius = 32
# framerate = 60
# speed = 500
# deltaTime = 1 / framerate
# joyTolerance = 0.2

# --- Main event loop
# for event in pygame.event.get():
# 	if event.type == pygame.QUIT:
# 		running = False
# 	if event.type == pygame.KEYDOWN:
# 		if event.key == pygame.K_r:
# 			player.sprite.set_anim_framerate(-player.sprite.get_anim_framerate())
# 		if event.key == pygame.K_PAGEUP:
# 			player.sprite.set_anim_framerate(player.sprite.get_anim_framerate() + 5)
# 		if event.key == pygame.K_PAGEDOWN:
# 			player.sprite.set_anim_framerate(player.sprite.get_anim_framerate() - 5)
#
# # --- Game logic should go here
#
# # Input
# movement = [0.0, 0.0]
#
# if hasJoystick:
# 	# Use joystick if one exists
#
# 	# D-Pad (digital joystick)
# 	# hat = joystick.get_hat(0)
# 	# movement[0] = hat[0]
# 	# movement[1] = -hat[1]
#
# 	# Actual Joystick (analog joystick)
# 	movement[0] = joystick.get_axis(0)
# 	movement[1] = joystick.get_axis(1)
#
# 	# Tolerance check to correct hardware imprecision
# 	if abs(movement[0]) < joyTolerance:
# 		movement[0] = 0
#
# 	if abs(movement[1]) < joyTolerance:
# 		movement[1] = 0
#
# else:
# 	# Use keyboard if joystick does not exist
# 	pressedKeys = pygame.key.get_pressed()
#
# 	# Input logic for keys designed to zero out movement when
# 	# both keys on axis are pressed (up/down or left/right)
# 	if pressedKeys[pygame.K_a] or pressedKeys[pygame.K_LEFT]:
# 		movement[0] -= 1
#
# 	if pressedKeys[pygame.K_d] or pressedKeys[pygame.K_RIGHT]:
# 		movement[0] += 1
#
# 	if pressedKeys[pygame.K_w] or pressedKeys[pygame.K_UP]:
# 		movement[1] -= 1
#
# 	if pressedKeys[pygame.K_s] or pressedKeys[pygame.K_DOWN]:
# 		movement[1] += 1
#
# # Normalize movement
# sqMagnitude = (movement[0] * movement[0]) + (movement[1] * movement[1])
# if sqMagnitude > 1:
# 	magnitude = math.sqrt(sqMagnitude)
# 	movement[0] /= magnitude
# 	movement[1] /= magnitude
#
# # Apply movement modified by speed and delta time to position
# position[0] += movement[0] * speed * deltaTime
# position[1] += movement[1] * speed * deltaTime
#
# # Clamp position to screen
# if position[0] < 0 + circleRadius:
# 	position[0] = 0 + circleRadius
#
# if position[0] > size[0] - circleRadius:
# 	position[0] = size[0] - circleRadius
#
# if position[1] < 0 + circleRadius:
# 	position[1] = 0 + circleRadius
#
# if position[1] > size[1] - circleRadius:
# 	position[1] = size[1] - circleRadius
#
# player.update(deltaTime, position)
#
# # Debug position and delta time
# # print(str(position[0]) + " : " + str(position[1]) + " : " + str(deltaTime));
#
# # --- Screen-clearing code goes here
#
# # Here, we clear the screen to white. Don't put other drawing commands
# # above this, or they will be erased with this command.
#
# # If you want a background image, replace this clear with blit'ing the
# # background image.
# # screen.fill(WHITE)
# screen.blit(background, (0, 0))
#
# # --- Drawing code should go here
#
# # Draw a circle at position
# # pygame.draw.circle(screen, BLUE, [int(position[0]), int(position[1])], circleRadius)
# player.draw(screen)
#
# # --- Go ahead and update the screen with what we've drawn.
# pygame.display.flip()
#
# # --- Limit to 60 frames per second
# deltaTime = clock.tick_busy_loop(framerate) / 1000.0

######## HARD-CODED SPRITE LOCATION LISTS ##########


# Spinning ball
# self.sprites = self.spriteSheet.images_at(
#	 [
#		 (0, 0, 64, 64),
#		 (64, 0, 64, 64),
#		 (128, 0, 64, 64),
#		 (192, 0, 64, 64),
#		 (256, 0, 64, 64),
#		 (320, 0, 64, 64),
#		 (384, 0, 64, 64),
#		 (448, 0, 64, 64),
#		 (0, 64, 64, 64),
#		 (64, 64, 64, 64),
#		 (128, 64, 64, 64),
#		 (192, 64, 64, 64),
#		 (256, 64, 64, 64),
#		 (320, 64, 64, 64),
#		 (384, 64, 64, 64),
#		 (448, 64, 64, 64),
#		 (0, 128, 64, 64),
#		 (64, 128, 64, 64),
#		 (128, 128, 64, 64),
#		 (192, 128, 64, 64),
#		 (256, 128, 64, 64),
#		 (320, 128, 64, 64),
#		 (384, 128, 64, 64),
#		 (448, 128, 64, 64),
#		 (0, 192, 64, 64),
#		 (64, 192, 64, 64),
#		 (128, 192, 64, 64),
#		 (192, 192, 64, 64),
#		 (256, 192, 64, 64),
#		 (320, 192, 64, 64),
#		 (384, 192, 64, 64),
#		 (448, 192, 64, 64),
#	 ], [255, 0, 255]  # Color Key for alpha
# )
# self.spriteCount = 32

# Spinning paper
# self.sprites = self.spriteSheet.images_at(
#	 [
#		 (0, 0, 64, 64),
#		 (64, 0, 64, 64),
#		 (128, 0, 64, 64),
#		 (192, 0, 64, 64),
#		 (256, 0, 64, 64),
#		 (320, 0, 64, 64),
#		 (384, 0, 64, 64),
#		 (448, 0, 64, 64),
#		 (512, 0, 64, 64),
#		 (576, 0, 64, 64),
#	 ], [255, 0, 255]  # Color Key for alpha
# )
# self.spriteCount = 10

# Rollimg Paper
'''
self.sprites = self.spriteSheet.images_at(
	[
		(0, 64, 64, 64),
		(64, 64, 64, 64),
		(128, 64, 64, 64),
		(192, 64, 64, 64),
		(256, 64, 64, 64),
		(320, 64, 64, 64),
		(384, 64, 64, 64),
		(448, 64, 64, 64),
		(512, 64, 64, 64),
		(576, 64, 64, 64),
		(576, 64, 64, 64),
		(640, 64, 64, 64),
		(704, 64, 64, 64),
		(768, 64, 64, 64),
		(832, 64, 64, 64),
		(896, 64, 64, 64),
	], [255, 0, 255]  # Color Key for alpha
)
self.spriteCount = 16
'''
