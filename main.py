import pygame 
import sys    


pygame.init()

def create_window():
    window_width = 800
    window_height = 800
    screen = pygame.display.set_mode((window_width, window_height))  
    pygame.display.set_caption("mini project 2")  
    return screen

screen = create_window()

white = (255, 255, 255)
black = (0, 0, 0)


running = True

while running:






    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

 
    screen.fill(white)


    pygame.display.update()

pygame.quit()
sys.exit()
