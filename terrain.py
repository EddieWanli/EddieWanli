import pygame
import random
grass = pygame.image.load("images/e.jpg")
def gen_world(screen):
    for x in range(0, 1000, 50):
        for y in range(500, 750, 50):
            offset_x = random.randint(0,20)
            offset_y = random.randint(0,20)
            x = random.randint(0, 1000)
            y = random.randint(0, 750)
            screen.blit(grass, (x + offset_x, y + offset_y))

