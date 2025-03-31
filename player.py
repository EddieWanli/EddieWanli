import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, sprite_list):
        super().__init__()
        self.sprites = []
        for sprite in sprite_list:
            self.sprites.append(sprite)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.15

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False

        self.image = self.sprites[int(self.current_sprite)]



