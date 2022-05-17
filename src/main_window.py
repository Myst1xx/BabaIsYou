import sys

sys.path.append("C:/Users/leudanghuy/Documents/Python_Learning/Project/BabaIsYou/BabaIsYou/src")

import pygame
import os

current_dir = os.path.dirname(__file__)

from graphics import GameplayGraphic

class MainWindow:
    def __init__(self) -> None:
        pass

    def open_main_menu(self):
        pass

    def pop_up_win(self):
        win_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/you_win.png"))
        #win_banner_resized = pygame.transform.scale(win_banner, (40,40))
        self.screen.blit(win_banner,[(self.screen.get_width()-win_banner.get_width())/2,(self.screen.get_height()-win_banner.get_height())/2])

        reset_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/reset_game.png"))
        reset_button = pygame.transform.scale(reset_button, (reset_button.get_width()/2,reset_button.get_height()/2))
        self.screen.blit(reset_button,[(self.screen.get_width()-reset_button.get_width())*0.5,(self.screen.get_height()-reset_button.get_height())*0.8])

    def pop_up_lose(self):
        lose_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/you_lose.png"))
        #lose_banner_resized = pygame.transform.scale(lose_banner, (40,40))
        self.screen.blit(lose_banner,[(self.screen.get_width()-lose_banner.get_width())/2,(self.screen.get_height()-lose_banner.get_height())/2])

        reset_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/reset_game.png"))
        reset_button = pygame.transform.scale(reset_button, (reset_button.get_width()/2,reset_button.get_height()/2))
        self.screen.blit(reset_button,[(self.screen.get_width()-reset_button.get_width())*0.5,(self.screen.get_height()-reset_button.get_height())*0.8])

    def start_game(self, level):
        self.running = True
        pygame.init()
        logo = pygame.image.load(os.path.join(current_dir, "../resources/graphics/baba.png"))
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Baba Is You")

        self.gameplay_graphic = GameplayGraphic(10,20)
        if level == 1:
            self.gameplay_graphic.load_map(os.path.join(current_dir, '../resources/maps/map1.csv'), os.path.join(current_dir, '../resources/maps/map1.info'))
        elif level == 2:
            self.gameplay_graphic.load_map(os.path.join(current_dir, '../resources/maps/map2.csv'), os.path.join(current_dir, '../resources/maps/map2.info'))
        
        self.gameplay_graphic.get_rules()
        self.gameplay_graphic.apply_rules()

        self.window_width = self.gameplay_graphic.n_cols*40
        self.window_height = self.gameplay_graphic.n_rows*40

        # create a surface on screen that has the size of window
        self.screen = pygame.display.set_mode((self.window_width
        ,self.window_height))

        self.gameplay_graphic.render(self.screen)
        pygame.display.update()

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                self.process_event(event)

            pygame.display.update()

    def process_event(self, event: pygame.event):
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            print("exit")
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            print(event.button)
            print(event.touch)
        # movement when press keys: A, D, S, W
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.gameplay_graphic.move_left()
            elif event.key == pygame.K_s:
                self.gameplay_graphic.move_down()
            elif event.key == pygame.K_d:
                self.gameplay_graphic.move_right()
            elif event.key == pygame.K_w:
                self.gameplay_graphic.move_up()
            
            self.screen.fill(('black'))
            self.gameplay_graphic.get_rules()
            self.gameplay_graphic.apply_rules()
            self.gameplay_graphic.render(self.screen)
            
            # check win / check lose after a movement and re-apply rules if it's not the case
            if self.gameplay_graphic.check_win():
                self.pop_up_win()
            elif self.gameplay_graphic.check_lose():
                self.pop_up_lose()

if __name__ == '__main__':
    main = MainWindow()
    main.start_game(2)
    main.run_game()