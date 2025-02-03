import pygame
# button class
class Button:
    def __init__(self, text, x, y, font, screen, colour):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.screen = screen
        self.colour = colour
        self.rect = pygame.Rect(self.x, self.y, 200, 50)

    def draw(self):
        button_text = self.font.render(self.text, True, "Black")
        text_rect = button_text.get_rect(center=self.rect.center)
        if self.check_hover():
            pygame.draw.rect(self.screen, "dark grey", self.rect, 0, 5)
        else:
            pygame.draw.rect(self.screen, self.colour, self.rect, 0, 5)
        pygame.draw.rect(self.screen, "black", self.rect, 2, 5)
        self.screen.blit(button_text, text_rect)

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect((self.x, self.y), (200,50))
        return button_rect.collidepoint(mouse_pos)

    def check_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.Rect((self.x, self.y), (200, 50))
        if left_click and button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False




