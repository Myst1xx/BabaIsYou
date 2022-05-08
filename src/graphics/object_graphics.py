import sys
sys.path.append("C:/Users/leudanghuy/Documents/Python_Learning/Project/BabaIsYou/BabaIsYou/src")

from gameplay import Baba, Rock, Water, Skull, Wall, Flag, Word

import pygame
import os

current_dir = os.path.dirname(__file__)

class BabaGraphic(Baba):
    def render(self, window, x, y):
        baba_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba.png"))

        #baba_image_resized = pygame.transform.scale(baba_image, (baba_image.get_width()/6,baba_image.get_height()/6))
        baba_image_resized = pygame.transform.scale(baba_image, (40,40))

        window.blit(baba_image_resized,[x,y])

class RockGraphic(Rock):
    def render(self, window, x, y):
        rock_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/rock.png"))

        rock_image_resized = pygame.transform.scale(rock_image, (40,40))

        window.blit(rock_image_resized,[x,y])

class WaterGraphic(Water):
    def render(self, window, x, y):
        water_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/water.png"))

        water_image_resized = pygame.transform.scale(water_image, (40,40))

        window.blit(water_image_resized,[x,y])

class SkullGraphic(Skull):
    def render(self, window, x, y):
        skull_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/skull.png"))

        skull_image_resized = pygame.transform.scale(skull_image, (40,40))

        window.blit(skull_image_resized,[x,y])

class WallGraphic(Wall):
    def render(self, window, x, y):
        wall_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/wall.png"))

        wall_image_resized = pygame.transform.scale(wall_image, (40,40))

        window.blit(wall_image_resized,[x,y])

class FlagGraphic(Flag):
    def render(self, window, x, y):
        flag_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/flag.png"))

        flag_image_resized = pygame.transform.scale(flag_image, (40,40))

        window.blit(flag_image_resized,[x,y])

class WordGraphic(Word):
    def render(self, window, x, y):
        png_file_name = "../../resources/graphics/" + self.value.upper() + "-w.png"

        png_image = pygame.image.load(os.path.join(current_dir, png_file_name))

        png_image_resized = pygame.transform.scale(png_image,(40,40))

        window.blit(png_image_resized, [x,y])


if __name__ == "__main__":
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba.png"))
    logo_resized = pygame.transform.scale(logo, (960,720))
    logo_width = logo_resized.get_width()
    logo_height = logo_resized.get_height()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Baba Is You")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((960,720), pygame.RESIZABLE)

    first_of_baba = BabaGraphic('you')
    first_of_wall = WallGraphic('wall')
    first_of_skull = SkullGraphic('skull')
    first_of_water = WaterGraphic('water')
    word_is = WordGraphic('is')

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        first_of_baba.render(screen, 70, 95)
        first_of_skull.render(screen, 100,200)
        first_of_wall.render(screen, 600,10)
        first_of_water.render(screen, 589,322)
        word_is.render(screen,652,679)

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print("exit")
                running = False
        
        pygame.display.update()