import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(9):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/spider", "0" + add_str + ".png")),
        (24, 24)))


class Spider(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "spider"
        self.money = 4
        self.imgs = imgs[:]
        self.max_health = 1
        self.health = self.max_health


