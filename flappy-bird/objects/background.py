import pygame
import assets
import configs
from layer import Layer


class Background(pygame.sprite.Sprite):
    def __init__(self, index , *groups):
        self._layer = Layer.OBSTACLE
        super().__init__(*groups)  # Önce Sprite sınıfını başlat

        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))

    def update(self):
        self.rect.x -= 1  # Arka planı sola kaydır
        if self.rect.right <= 0:  # Eğer tamamen ekran dışına çıktıysa
            self.rect.x = configs.SCREEN_WIDTH  # Tekrar sağdan başlat
