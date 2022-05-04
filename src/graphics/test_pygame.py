# import the pygame module, so you can use it
import pygame
import os

current_dir = os.path.dirname(__file__)
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/Meme1.jpg"))
    logo_resized = pygame.transform.scale(logo, (960,720))
    logo_width = logo_resized.get_width()
    logo_height = logo_resized.get_height()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Baba Is You")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((960,720), pygame.RESIZABLE)
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        screen.blit(logo_resized,((screen_width-logo_width)/2,(screen_height-logo_height)/2))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print("exit")
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                print(event.button)
                print(event.touch)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("move left")
                elif event.key == pygame.K_s:
                    print("move down")
                elif event.key == pygame.K_d:
                    print("move right")
                elif event.key == pygame.K_w:
                    print("move up")
        
        pygame.display.update()

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()