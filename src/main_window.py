import sys

sys.path.append("C:/Users/leudanghuy/Documents/Python_Learning/Project/BabaIsYou/BabaIsYou/src")

import pygame
import os

current_dir = os.path.dirname(__file__)

from graphics import GameplayGraphic

class MainWindow:
    def __init__(self) -> None:
        pass

    def start_game(self, level):
        pygame.init()
        logo = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba.png"))
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Baba Is You")

        self.gameplay_graphic = GameplayGraphic(10,20)
        if level == 1:
            self.gameplay_graphic.load_map(os.path.join(current_dir, '../resources/maps/map1.csv'), os.path.join(current_dir, '../resources/maps/map1.info'))
        elif level == 2:
            self.gameplay_graphic.load_map(os.path.join(current_dir, '../resources/maps/map2.csv'), os.path.join(current_dir, '../resources/maps/map2.info'))

        self.window_width = self.gameplay_graphic.n_cols*40
        self.window_height = self.gameplay_graphic.n_rows*40

        # create a surface on screen that has the size of window
        self.screen = pygame.display.set_mode((self.window_width
        ,self.window_height))

    def run_game(self):
        pass

    def process_event(self, event):
        pass