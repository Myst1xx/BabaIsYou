import sys
import pygame
import os

current_dir = os.path.dirname(__file__)

sys.path.append(os.path.join(current_dir,".."))

from gameplay import Baba, Rock, Water, Skull, Wall, Flag, Word



class BabaGraphic(Baba):
    # static variable
    baba_image = None

    def render(self, window, x, y):
        if BabaGraphic.baba_image == None:    
            BabaGraphic.baba_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba.png"))

        baba_image_resized = pygame.transform.scale(BabaGraphic.baba_image, (40,40))

        window.blit(baba_image_resized,[x,y])

class RockGraphic(Rock):
    rock_image = None

    def render(self, window, x, y):
        if RockGraphic.rock_image == None:
            RockGraphic.rock_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/rock.png"))

        rock_image_resized = pygame.transform.scale(RockGraphic.rock_image, (40,40))

        window.blit(rock_image_resized,[x,y])

class WaterGraphic(Water):
    water_image = None

    def render(self, window, x, y):
        if WaterGraphic.water_image == None:
            WaterGraphic.water_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/water.png"))

        water_image_resized = pygame.transform.scale(WaterGraphic.water_image, (40,40))

        window.blit(water_image_resized,[x,y])

class SkullGraphic(Skull):
    skull_image = None

    def render(self, window, x, y):
        if SkullGraphic.skull_image == None:
            SkullGraphic.skull_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/skull.png"))

        skull_image_resized = pygame.transform.scale(SkullGraphic.skull_image, (40,40))

        window.blit(skull_image_resized,[x,y])

class WallGraphic(Wall):
    wall_image = None

    def render(self, window, x, y):
        if WallGraphic.wall_image == None:
            WallGraphic.wall_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/wall.png"))

        wall_image_resized = pygame.transform.scale(WallGraphic.wall_image, (40,40))

        window.blit(wall_image_resized,[x,y])

class FlagGraphic(Flag):
    flag_image = None

    def render(self, window, x, y):
        if FlagGraphic.flag_image == None:
            FlagGraphic.flag_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/flag.png"))

        flag_image_resized = pygame.transform.scale(FlagGraphic.flag_image, (40,40))

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