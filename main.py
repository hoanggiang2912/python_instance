import pygame

from pygame.locals import *

import os

import sys

import math


pygame.init()


W, H = 800, 447

win = pygame.display.set_mode((W,H))

pygame.display.set_caption('Side Scroller')


bg = pygame.image.load(os.path.join('images','bg.png')).convert()

bgX = 0

bgX2 = bg.get_width()


clock = pygame.time.Clock()

class player (object): 
  run = [
    pygame.image.load(os.path.join('images','run1.png')).convert_alpha(),
    pygame.image.load(os.path.join('images','run2.png')).convert_alpha(),
  ]