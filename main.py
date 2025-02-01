# initialize pygame modules
import pygame
from button import Button
pygame.init()

 
# create game window
width = 1000
height = 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Terraworld")

# main menu control
main_menu = False

# time controls
fps = 60
timer = pygame.time.Clock()

# font
font = pygame.font.SysFont("freesansbold.ttf", 30)

def draw_game():
    button = Button("Main menu", 370, 450, 230, 450)
    button.draw()

# game loop
run = True
while run:
    screen.fill("light blue")
    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()



