import pygame as pg
WIDTH = 1024
HEIGHT = 768
TITLE = "Best game evah!!!"
TILESIZE = 32
FPS = 30

# Colors
BGCOLOR = (0, 120, 250)
WHITE = (255,255,255)
GREEN = (0,120,0)
RED = (255,0,0)
BLACK = (0,0,0)

# Player settings
PLAYER_SPEED = 300
PLAYER_HIT_RECT = pg.Rect(0,0, TILESIZE-5, TILESIZE-5)

#Mob settings
MOB_HIT_RECT = pg.Rect(0,0, TILESIZE-5, TILESIZE-5)