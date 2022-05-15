import sys

sys.path.append("C:/Users/leudanghuy/Documents/Python_Learning/Project/BabaIsYou/BabaIsYou/src")

import pygame
import os
import numpy as np
import pandas as pd

current_dir = os.path.dirname(__file__)

from gameplay import Gameplay, Tile
from graphics.object_graphics import BabaGraphic, RockGraphic, WaterGraphic, SkullGraphic, WallGraphic, FlagGraphic, WordGraphic

class GameplayGraphic(Gameplay):
    def load_map(self, file_map, file_info):
        self.file_map = file_map
        self.file_info = file_info

        with open(file_info) as f:
            self.n_rows = int(f.readline())
            self.n_cols = int(f.readline())
            # reset and resize tiles to fit dimensions in info file.
            self.tiles = np.zeros((self.n_rows, self.n_cols), dtype=object)
            for i in range(self.n_rows):
                for j in range(self.n_cols):
                    self.tiles[i,j] = Tile()
        
        map_data = pd.read_csv(file_map, header = None)
        map_data_array = np.array(map_data, dtype = str)
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                # split the words in a tile to an array by the '/'
                value_list = map_data_array[r,c].split('/')
                for value in value_list:
                    if value == '':
                        continue
                    elif value == 'baba':
                        self.tiles[r,c].add_object(BabaGraphic())
                    elif value == 'rock':
                        self.tiles[r,c].add_object(RockGraphic())
                    elif value == 'water':
                        self.tiles[r,c].add_object(WaterGraphic())
                    elif value == 'skull':
                        self.tiles[r,c].add_object(SkullGraphic())
                    elif value == 'wall':
                        self.tiles[r,c].add_object(WallGraphic())
                    elif value == 'flag':
                        self.tiles[r,c].add_object(FlagGraphic())
                    elif value.isupper():
                        self.tiles[r,c].add_object(WordGraphic(value.lower()))

    def render(self, window):
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                tile = self.tiles[r,c]
                for obj in tile.objects:
                    obj.render(window, 40*c, 40*r)

if __name__ == '__main__':
    pygame.init()
    logo = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba.png"))
    logo_resized = pygame.transform.scale(logo, (960,720))
    logo_width = logo_resized.get_width()
    logo_height = logo_resized.get_height()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Baba Is You")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((960,720), pygame.RESIZABLE)

    gg_test = GameplayGraphic(10,20)
    gg_test.load_map(os.path.join(current_dir, '../../resources/maps/map1.csv'), os.path.join(current_dir, '../../resources/maps/map1.info'))

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print("exit")
                running = False

        gg_test.render(screen)
        
        pygame.display.update()