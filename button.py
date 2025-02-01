import pygame
# button class
class Button:
    def __init__(self, text, x, y, width, height, colour):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.button = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen,"light grey",self.button, 0, 5)
        pygame.draw.rect(screen,"light grey",self.button, 5, 5)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255,255,255))
        screen.blit(text, [self.x + 15, self.y + 7])

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False




