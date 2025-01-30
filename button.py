import pygame

# colours
white = (255, 255, 255)
black = (0, 0, 0)
light_blue = (0, 51, 102)

# button class
class Button:
    def __init__(self, text, x, y, width, height, action = None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action

