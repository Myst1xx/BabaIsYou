import sys

sys.path.append("C:/Users/leudanghuy/Documents/Python_Learning/Project/BabaIsYou/BabaIsYou/src")

import pygame
import os

current_dir = os.path.dirname(__file__)

from graphics import GameplayGraphic

class MainWindow:
    def __init__(self) -> None:
        pygame.init()
        logo = pygame.image.load(os.path.join(current_dir, "../resources/graphics/baba.png"))
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Baba Is You")

        self.window_width = 1400
        self.window_height = 800

        # create a surface on screen that has the size of window
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        self.background_music = pygame.mixer.music.load('C:/Users/leudanghuy/Documents/Python_Learning/Project/BabaIsYou/BabaIsYou/resources/graphics/Music.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def open_main_menu(self):
        self.scene = 'menu'

        self.screen.fill(('black'))

        # pop up main menu banner
        main_menu_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/banner_main_menu.png"))
        self.screen.blit(main_menu_banner,[(self.screen.get_width()-main_menu_banner.get_width())*0.5,(self.screen.get_height()-main_menu_banner.get_height())*0.25])

        # pop up level 1 button in menu
        self.lv1_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/level_1.png"))
        self.lv1_button = pygame.transform.scale(self.lv1_button, (self.lv1_button.get_width()/2,self.lv1_button.get_height()/2))
        self.lv1_button_rect = self.lv1_button.get_rect(center=(self.screen.get_width()*0.25,self.screen.get_height()*0.75))
        self.screen.blit(self.lv1_button, self.lv1_button_rect)

        # pop up level 2 button in menu
        self.lv2_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/level_2.png"))
        self.lv2_button = pygame.transform.scale(self.lv2_button, (self.lv2_button.get_width()/2,self.lv2_button.get_height()/2))
        self.lv2_button_rect = self.lv2_button.get_rect(center=(self.screen.get_width()*0.75,self.screen.get_height()*0.75))
        self.screen.blit(self.lv2_button, self.lv2_button_rect)

        pygame.display.update()

        getting_level = True
        self.running = True

        while getting_level and self.running:
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.level = self.get_level(position)
                    if self.level > 0:
                        self.scene = 'ingame'
                        getting_level = False
            
            pygame.display.update()

        if self.scene == 'ingame':
            self.open_gameplay(self.level)

    def pop_up_win(self):
        win_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/you_win.png"))
        self.screen.blit(win_banner,[(self.screen.get_width()-win_banner.get_width())/2,(self.screen.get_height()-win_banner.get_height())/2])

        reset_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/reset_game.png"))
        reset_button = pygame.transform.scale(reset_button, (reset_button.get_width()/2,reset_button.get_height()/2))
        self.reset_button_rect = reset_button.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()*0.75))
        self.screen.blit(reset_button, self.reset_button_rect)

    def pop_up_lose(self):
        lose_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/you_lose.png"))
        self.screen.blit(lose_banner,[(self.screen.get_width()-lose_banner.get_width())/2,(self.screen.get_height()-lose_banner.get_height())/2])

        reset_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banners/reset_game.png"))
        reset_button = pygame.transform.scale(reset_button, (reset_button.get_width()/2,reset_button.get_height()/2))
        self.reset_button_rect = reset_button.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()*0.75))
        self.screen.blit(reset_button, self.reset_button_rect)

    def get_level(self, position: pygame.mouse):
        if self.lv1_button_rect.collidepoint(position):
            return 1
        elif self.lv2_button_rect.collidepoint(position):
            return 2
        else:
            return -1

    def open_gameplay(self, level):
        self.scene = 'ingame'

        self.screen.fill(('black'))

        self.running = True

        self.gameplay_graphic = GameplayGraphic(10,20)
        if level == 1:
            self.gameplay_graphic.load_map(os.path.join(current_dir, '../resources/maps/map1.csv'), os.path.join(current_dir, '../resources/maps/map1.info'))
        elif level == 2:
            self.gameplay_graphic.load_map(os.path.join(current_dir, '../resources/maps/map2.csv'), os.path.join(current_dir, '../resources/maps/map2.info'))
        
        self.gameplay_graphic.get_rules()
        self.gameplay_graphic.apply_rules()

        self.gameplay_graphic.render(self.screen)
        pygame.display.update()

        self.run_gameplay()

        if self.scene == 'endgame':
            self.process_endgame_screen()

    def run_gameplay(self):
        while self.running and self.scene == 'ingame':
            for event in pygame.event.get():
                self.process_event(event)

            pygame.display.update()

    def process_event(self, event: pygame.event):
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            self.running = False
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
                self.scene = 'endgame'
            elif self.gameplay_graphic.check_lose():
                self.pop_up_lose()
                self.scene = 'endgame'

    def process_endgame_screen(self):
        self.scene == 'endgame'
        while self.running and self.scene == 'endgame':
            for event in pygame.event.get():
                position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.reset_button_rect.collidepoint(position):
                        self.scene = 'menu'
        pygame.display.update()
        if self.scene == 'menu':
            self.open_main_menu()

if __name__ == '__main__':
    main = MainWindow()
    main.open_main_menu()
    # main.start_game(2)
    # main.run_game()