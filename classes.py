#-*- coding: utf-8 -*-

"""Help MacGyver Escape Labyrinth game classes."""

# TODO: import libraries

import pygame
from pygame.locals import *
from constants import *
from random import *


# TODO: create class Level to generate game level & display it from read file.
class Level:
	"""Class to create a level in the game."""
	def __init__(self, file):
		# Define attibute file (for lvl).
		self.file = file
		# Define attribute grid.
		self.grid = 0
		# define attribute empty tuples list which runs twice: once for--
		# --columns & once for lines (x,y) for the empty spots in the--
		# --labyrinth where the in game objects can randomly spawn.
		self.free = [] # free = free sprites.

	# Method 1 = generates a game level according to lvl file in an--
	# --attribute 'structure'.
	def generate(self):
		"""Method which generates a game level according to the file read.
		We create a general list containing a line per line list to display."""
		
		# Open the file and read ('r') it.
		with open(self.file, 'r') as file:
			grid_level = []
			# Initialize coordinates at -1 because the grid starts at 0--
			# --and I will append +1 to columns and lines.
			x = -1
			y = -1
			# Run the lines in the file.
			for line in file:
				line_level = []
				# Count lines in the grid.
				y += 1
				# A new line starts, columns restart.
				x = -1
				# Run each sprite/letters in the file.
				for sprite in line:
					# Count the columns in the grid.
					x += 1 
					# Ignore '\n' at the end of each line (not a sprite)
					if line != '\n':
						# Add sprite to lines list
						line_level.append(sprite)
					# Check if sprite is a free spot in the grid.
					if sprite == '0':
						# If sprite is free add sprite to list free.
						self.free.append((x,y))
				# Add lines to level list.
				grid_level.append(line_level)
			# Save the grid.
			self.grid = grid_level
		# Print the structure of the grid in terminal.
		print(self.grid)

	# Method 2 = displays labyrinth aka game level (we only have one).
	def display(self, display):
		"""Method which displays game level according to grid list returned
		by generate()."""
		
		# Load images.
		wall = pygame.image.load(image_wall).convert()
		start = pygame.image.load(image_start).convert()
		# convert_alpha for transparent images.
		end = pygame.image.load(image_end).convert_alpha()

		# Run level list.
		line_nb = 0
		for line in self.grid:
			# Run lines lists.
			sprite_nb = 0
			for sprite in line:
				# Calculate real position in pixels per column.
				x = sprite_nb * sprite_size
				# Calculate real position in pixels per line.
				y = line_nb * sprite_size
				if sprite == 'w': # w = wall.
					display.blit(wall, (x,y))
				elif sprite == 's': # s = start.
					display.blit(start, (x,y))
				elif sprite == 'e': # e = end = guardian.png = is transparent.
					display.blit(end, (x,y))
				# Add one sprite.
				sprite_nb += 1
			# Add one line.
			line_nb += 1


# TODO: create class Character to display MacGyver and make him move.
class Character:
	"""Class that creates a character."""
	
	# Define MacGyver with self attributes =
	def __init__(self, face, level):
		# Character sprite (convert_alpha = transparency)
		self.face = pygame.image.load(ig_macgyver).convert_alpha()
		# Character's position in sprites
		self.sprite_x = 0
		self.sprite_y = 0
		# Character's position in pixels
		self.x = 0
		self.y = 0
		# Game level character is in (we only have the one here)
		self.level = level
		# Counter for the 3 in game objects MacGyver must pick up.
		self.ig_object = 0

	# Method 1 = to move MacGyver in the game 
	def move(self, direction):
		"""Method to move MacGyver and to pick up in game objects."""

		# Check if MacGyver is on a sprite that has an in game object on it.
		# 'i' = item.
		if self.level.grid[self.sprite_y][self.sprite_x] == 'i':
			print("I've picked up an object! YESSS!!!")
			# Add 1 to in game object counter.
			self.ig_object += 1
			print("I have {} objects.".format(self.ig_object))
			# Replace 'i' (item sprite) by '0'(free sprite) on the background--
			# --to make in game objects disappear once MacGyver has picked--
			# --them up.
			self.level.grid[self.sprite_y][self.sprite_x] = '0'

		# Moving right
		if direction == 'right':
			 # Make sure MacGyver doesn't go past the screen
			if self.sprite_x < (sprite_per_side - 1):
				 # Checks destination sprite is not a wall
				if self.level.grid[self.sprite_y][self.sprite_x+1] != 'w':
					# Move one sprite
					self.sprite_x += 1
					# Computing of MacGyver's 'real' position in pixels
					self.x = self.sprite_x * sprite_size

		# Moving left
		if direction == 'left':
			if self.sprite_x > 0:
				if self.level.grid[self.sprite_y][self.sprite_x-1] != 'w':
					self.sprite_x -= 1
					self.x = self.sprite_x * sprite_size

		# Moving up
		if direction == 'up':
			if self.sprite_y > 0:
				if self.level.grid[self.sprite_y-1][self.sprite_x] != 'w':
					self.sprite_y -= 1
					self.y = self.sprite_y * sprite_size

		# Moving down
		if direction == 'down':
			if self.sprite_y < (sprite_per_side - 1):
				if self.level.grid[self.sprite_y+1][self.sprite_x] != 'w':
					self.sprite_y += 1
					self.y = self.sprite_y * sprite_size


class Item:
	"""Class that creates the in games items useful to the hero."""
	
	# Define 3 objects =	
	def __init__(self, level, n):
		
		# Choose a random sprite in list free for a random spot the in game--
		# --object can spawn on.
		position = choice(level.free) # Choice = random library.
		# Define position x for random in game object
		self.sprite_x = position[0]
		# Define position y for random in game object
		self.sprite_y = position[1]

		# Change sprite type '0' for sprite type 'i' so that in game objects--
		# --do not spawn on top of each other and they disappear when--
		# --MacGyver picks them up.
		# Grid is a list of list with form [[ line1], [line2],..., [line15]]--
		# --where each line is a list.
		# New line y and column x.
		level.grid[self.sprite_y][self.sprite_x] = 'i'
		# Print grid to visualize the free sprites 'i'.
		print(level.grid)

		# n means number and represents an attribute number strictly between--
		# --1 and 3 that are the in game objects/items.
		if n == 1 : # ig_object1.
			self.face = pygame.image.load(ig_object1).convert_alpha()
	
		elif n == 2 : # ig_object2.
			self.face = pygame.image.load(ig_object2).convert_alpha()
			
		elif n == 3 : #ig_object3.
			self.face = pygame.image.load(ig_object3).convert_alpha()
	
		# Item position in pixels.
		self.x = self.sprite_x * sprite_size
		self.y = self.sprite_y * sprite_size
		# Game level items are in (we only have the one here).
		self.level = level