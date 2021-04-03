import pygame as pg
import sys
import random

pg.init()

# Screen Specification parameters
SCREENSIZE = (720, 640)
CAPTIONS = "Raindrops"
BACKGROUND = (0, 30, 0)
BACKALPHA = 230

# Color palette
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

DISPSURFACE = pg.display.set_mode(SCREENSIZE, pg.SRCALPHA, 32)
pg.display.set_caption(CAPTIONS)

FPS = 50
CLOCK = pg.time.Clock()
