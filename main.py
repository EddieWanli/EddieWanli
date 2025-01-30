import pygame
# initiating pygame modules
pygame.init()

# assigning screen height and width (800 by 600 during development)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# setting screen height and width
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# loop for running the game
run = True

while run:

    pygame.draw.rect(screen, (255,0,0), player)
