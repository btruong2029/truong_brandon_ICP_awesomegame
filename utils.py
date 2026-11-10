import pygame as pg
from settings import *
from math import floor

# Map is read from "level1.txt", and as the file is read, the code knows whether to instantiate a wall, player, mob, coin, etc... based on the letter in the map
class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())
 
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE 


# Sprite sheet is used for character models/images, uses a 32 by 32 base image mapping, and x value multiplies with the amount of images added to the spritesheet
class Spritesheet: 
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x,y, width, height))
        new_image = pg.transform.scale(image, (width, height))
        image = new_image
        return image

#Timer used so particles know when to die/get killed from the moment of it's instantiation
class Timer:
    def __init__(self): # removed time parameter because it is already implemented in the class itself
        self.event_time = floor((pg.time.get_ticks())/1000)
    def get_delta(self):
        # returns difference in time in seconds from time of instantiation to now
        return floor((pg.time.get_ticks())/1000) - self.event_time