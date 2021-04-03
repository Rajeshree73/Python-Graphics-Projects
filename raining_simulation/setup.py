import pygame as pg
import sys
import random

# initialize py engine
pg.init()

SCREENSIZE = (720,640)
# Screen name
CAPTIONS = 'Raining Simulation'
BACKGROUND = (0,0,0)

# colour palatte 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKALPHA = 230

DISPSURFACE = pg.display.set_mode(SCREENSIZE, pg.SRCALPHA, 32) # 32= DEPTH
pg.display.set_caption(CAPTIONS)

FPS = 60
CLOCK = pg.time.Clock()

