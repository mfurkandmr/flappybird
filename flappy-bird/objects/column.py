import random

import pygame

import assets
import configs
from configs import SCREEN_WIDTH


class Column(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.gap = 100
        super().__init__(*groups)  # Önce Sprite sınıfını başlat

        self.sprite = assets.get_sprite("pipe-green")
        self.sprite_rect = self.sprite.get_rect()

        self.pipe_bottom = self.sprite
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(0,self.sprite_rect.height + self.gap))

        self.pipe_top = pygame.transform.flip(self.sprite, True, False)
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(0,0))

        self.image =pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap), pygame.SRCALPHA)


        self.image.blit(self.pipe_bottom, self.pipe_bottom_rect)
        self.image.blit(self.pipe_top, self.pipe_top_rect)

        sprite_floor_height = assets.get_sprite("floor").get_rect().height

        min_y = 100
        max_y = configs.SCREEN_HEIGHT - sprite_floor_height - 100

        self.rect = self.image.get_rect(midleft=(configs.SCREEN_WIDTH, random.uniform(min_y, max_y)))


        super().__init__(*groups)
    def update(self):
        self.rect.x -= 1

        if self.rect.right <= 0:
            self.kill()
