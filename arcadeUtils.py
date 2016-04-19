import pygame
import pygame.key
import pygame.draw
import pygame.sprite

import spritesheet

import math

def gen_sprite_list(numSprites, numSpritesPerRow, spriteXSize, spriteYSize, StartRow):
	#Generates locations of sprites on a sprite sheet given certian values, output 
	#can then be fed to the spriteSheet.images_at function as the first argument
	
	# numSpritesPerRow: self expl.
	# numSprites: self expl.
	# spriteYSize: self expl.
	# spriteXSize: self expl.
	# colorKey: self expl.
	# StartRow: Row the sprite starts on within the file (0 Based)
	# 


	i = 0 #iteration
	currRowOnSprite = 0 #Sprite within the current row its iterating on
	currRow = StartRow #Row it's iterating on, starting with arg
	currSpriteSheet = [] #Array of tuples of the locations of all the sprites, generated
	while i < numSprites:
		if currRowOnSprite < numSpritesPerRow:
			currSpriteSheet.append(((currRowOnSprite*spriteXSize),(currRow*spriteYSize),spriteXSize,spriteYSize))
			i +=1
			currRowOnSprite +=1
		else:
			currRowOnSprite = 0
			currRow +=1	
	return currSpriteSheet