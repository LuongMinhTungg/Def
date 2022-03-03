import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(19):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/golem", "0" + add_str + ".png")),
        (100, 100)))


class Golem(Enemy):

    def __init__(self):
        super().__init__()
        self.name = "golem"
        self.money = 400
        self.imgs = imgs[:]
        self.max_health = 50
        self.health = self.max_health




