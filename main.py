# This file was created by Brandon Truong
# Code inspired by Chris bradfield who was inspired by Notch

# Data types: boolean, JSON, strings,

# Input (events): Keyboard, mouse, right click, voice, power button, eye tracking, camera, gyroscoping,
# electrostatic, location, volume button, microphone, 

# Process: Cursor position, position of the player, score, enemy position, 
# Aim in FPS, 

# Output: Graphics - things are drawn, sound: jump, walking, power up,
# haptics

import pygame as pg #importing as pg to make typing pygame easier
from os import path
from settings import * #imports everything from settings.py
from sprites import * #imports everything from sprites.py
from utils import *
 
class Game: #initializing class Game
    def __init__(self):
        pg.init() #initializing pygame
        pg.mixer.init() #initializing pygame sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) #setting screen size to 800x600 from settings.py
        print("game initialized...")
        pg.display.set_caption(TITLE) #changing window name to TITLE from settings.py
        self.running = True
        self.playing = True
        self.clock = pg.time.Clock()
    def load_data(self, map):
        self.game_dir = path.dirname(__file__)
        self.img_dir = path.join(self.game_dir, 'ímages')
        self.snd_dir = path.join(self.game_dir, 'audio')
        self.map = Map(path.join(self.game_dir, map))
    def new(self):
        self.load_data('level1.txt')
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.wall = Wall(self, 2, 0) #puts self.cactus on top left corner
        self.mob = Mob(self, 5, 0)
 
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)
                if tile == 'M':
                    pass
                # if tile == 'P':
                #     Player(self, col, row)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "P":
                    Wall(self, col, row)

    def run(self):
        self.playing = True
        while self.playing: #will always be True until user exits game where self.running will become False
            self.dt = self.clock.tick(FPS) / 1000
            self.events() #when user launches game, self.running will be True, so it will run the events method
            #self.update()
            self.draw() #draws the background color
            self.update() #updates the movement of the white block
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: #changes the self.running to False to quit the game when the X button is clicked to close the window and quit the while loop in the run method
                if self.playing:
                    self.playing = False
                self.running = False
    def draw(self):
        self.screen.fill(BGCOLOR) #tells the code which color to fill the background
        self.all_sprites.draw(self.screen) #everything will be drawn on the screen
        pg.display.flip()
    def update(self):
        self.all_sprites.update() #updates the position of the block based on vx and vy
if __name__ == "__main__": #checks if we are in main.py and if we are in main.py, it will initialize Game
    g = Game()
 
while g.running: #keeps the window open forever
    g.new()
    g.run()