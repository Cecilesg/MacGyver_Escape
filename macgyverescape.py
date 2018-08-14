#-*- coding: utf-8 -*-

"""
Helping MacGyver Escape Labyrinth Game.

In this game, the player must pick up 3 objects along the way in the labyrinth
then progress to face the guardian so they can escape and end the game.

Script: Python3
Files: macgyverescape.py, classes.py, constants.py, lvl + images
"""

# TODO: import libraries.
import pygame
from pygame.locals import *
from random import *

from classes import *
from constants import *

# TODO: initialize Pygame library.
pygame.init()

# TODO: open game display window.
display = pygame.display.set_mode((display_per_side, display_per_side))
# Game icon.
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)
# Game title.
pygame.display.set_caption(game_name)
# Allow continuous pressing of movement keys in the game display window.
pygame.key.set_repeat(400, 30) # Delay in millisec of how long a key is--
# --pressed before char. mvt & time in millisec between each char. mvt.

# TODO: create game global loop = algorithm.
carry_on = 1
while carry_on:
	# Load and display game menu.
	game_menu = pygame.image.load(image_game_menu).convert()
	display.blit(game_menu, (0,0))

	# Refresh.
	pygame.display.flip()

	# Reset variables to 1 every lap of the loop.
	carry_on_game = 1
	carry_on_game_menu = 1

	# TODO: create game menu loop.
	while carry_on_game_menu:

		# Limit loop speed.
		pygame.time.Clock().tick(30)

		# TODO: give user possibility to choose event in game menu.
		for event in pygame.event.get():

			# If user quits, variables in game menu loop all go to 0.
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				carry_on_game_menu = 0
				carry_on_game = 0
				carry_on = 0
				choice = 0 # Variable for choice in game menu.

			# Launch game level aka labyrinth.
			elif event.type == KEYDOWN and event.key == K_RETURN:
				# User leaves game_menu and starts to play.
				carry_on_game_menu = 0
				# Loads labyrinth as designed in file read 'lvl'.
				choice = 'lvl'

	# While in loop, check if user chose to play so as not to load the game.
	# If they chose to quit.
	if choice != 0:
		# Then load background.
		background = pygame.image.load(image_background).convert()

		# Generate game level from file.
		level = Level(choice)
		level.generate()
		level.display(display)

		# Generate MacGyver.
		macgyver = Character(ig_macgyver, level)

		# Generate the items MacGyver must pick up.
		object1 = Item(level,1)
		object2 = Item(level,2)
		object3 = Item(level,3)

	# TODO: Create game loop.
	while carry_on_game:

		# Limit loop speed.
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			# If user quits game then turn carry_on_game & carry_on to 0 to--
			# --close display window.
			if event.type == QUIT:
				carry_on_game = 0
				carry_on = 0

			elif event.type == KEYDOWN:
				# If user presses ESCAPE = return to Game_Menu.
				if event.key == K_ESCAPE:
					carry_on_game = 0
					carry_on = 1

				# If user uses arrow keys then move MacGyver.
				elif event.key == K_RIGHT:
					macgyver.move('right')
				elif event.key == K_LEFT:
					macgyver.move('left')
				elif event.key == K_UP:
					macgyver.move('up')
				elif event.key == K_DOWN:
					macgyver.move('down')

		# Display new positions.
		display.blit(background, (0,0))
		level.display(display)
		display.blit(macgyver.face, (macgyver.x, macgyver.y))
		
		# Display in game objects only if there is 'i' for free item sprite.
		if level.grid[object1.sprite_y][object1.sprite_x] == 'i':
			display.blit(object1.face, (object1.x, object1.y))
		if level.grid[object2.sprite_y][object2.sprite_x] == 'i':
			display.blit(object2.face, (object2.x, object2.y))
		if level.grid[object3.sprite_y][object3.sprite_x] == 'i':
			display.blit(object3.face, (object3.x, object3.y))
		
		# Refresh.
		pygame.display.flip()

		# Victory = Game_Menu.
		if level.grid[macgyver.sprite_y][macgyver.sprite_x] == 'e':
				# Labyrinth loop ends.
				carry_on_game = 0
				# Global game loop carries on.
				carry_on = 1
				# Back to game menu for user choice.
				carry_on_game_menu = 1
		
		display.blit(game_menu, (0,0))
