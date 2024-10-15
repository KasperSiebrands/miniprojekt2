import pygame 
import sys    
from map import draw_map  

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


screen.fill(white)
draw_map(screen)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

 




    pygame.display.update()

pygame.quit()
sys.exit()
