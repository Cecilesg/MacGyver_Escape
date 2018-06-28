#-*- coding: utf-8 -*-

"""
Helping MacGyver Escape Labyrinth Game.

In this game, the player must pick up 3 objects along the way in the labyrinth
then progress to face the guardian so they can escape and end the game.

Script: Python3
Files: macgyver.py, classes.py, constants.py, level1 + images
"""

# TODO: import libraries
import pygame
from pygame.locals import *

from classes import *
from constants import *

# TODO: initialize Pygame library
pygame.init()

# TODO: open game display window
display = pygame.display.set_mode((display_per_side, display_per_side))
# Game icon
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)
# Game title
pygame.display.set_caption(game_name)